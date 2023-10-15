import time
from itertools import chain, combinations, product
import copy
import itertools

def removeEmpty(listWithEmpty:list):
    while [] in listWithEmpty:
        listWithEmpty.remove([])
    return listWithEmpty

def writeList(path2file:str, objs:list):
    f = open(path2file, "w", newline='', encoding='utf-8')
    for obj in objs:
        f.write(f"{obj}\n")
    f.close()    

def writeNestedList(path2file:str, objs:list):
    f = open(path2file, "w", newline='', encoding='utf-8')
    for obj in objs:
        for sObjs in obj:
            f.write("\t%s\n" %sObjs)
        f.write("\n\n")
    f.close()    

def rotatePick(pick:list, n:int):
    newPick = []
    for tick in pick:
        newPick.append((tick + n) % 32)
    return newPick

def matchPickToLock(pick:list, lock:list):
    solution = []
    for hole in lock:
        diff = hole - pick[0]
        newPick = rotatePick(pick, diff)
        if all(tick in lock for tick in newPick):
            solution.append(newPick[0] - pick[0])
    return solution

def newMatchPickToLock(lock:list, pick:list):
    solution = []
    for hole in lock:
        diff = hole - pick[1][0]
        newPick = [pick[0], rotatePick(pick[1], diff)]
        if all(tick in lock for tick in newPick[1]):
            solution.append(newPick)
    return solution
        
def powerSet(s:list):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def fixPicks(picks:list):
    newFormat = []
    for p, pick in enumerate(picks):
        newFormat.append([p+1, pick])
    return newFormat

def combinePicks(picks:list):
    powerset = powerSet(picks)
    listSet = []
    for sSet in powerset:
        listSet.append(list(sSet))
    return listSet

def countCombTicks(comb:list):
    if len(comb) == 0:
        return -1
    tickCount = 0
    for pick in comb:
            tickCount += len(pick[1])
    return tickCount

def filterCombinations(combs:list, locks:list):
    validCombs = []
    for lock in locks:
        validCombs.append([])
        for comb in combs:
            if len(lock) == countCombTicks(comb):
                validCombs[-1].append(comb)
    return validCombs

def cartesianProduct(validCombs:list):
    product = list(itertools.product(*validCombs))
    for i, p in enumerate(product):
        product[i] = list(p)
    return product

def filterCartesian(cartesian:list, locks:list):
    filtered = []
    for product in cartesian:
        usedPicks = []
        invalidProduct = False
        for l, lock in enumerate(product):
            for pick in lock:
                if pick[0] in usedPicks:
                    invalidProduct = True
                    break
                elif matchPickToLock(pick[1], locks[l]) == []:
                    invalidProduct = True
                    break
                else:
                    usedPicks.append(pick[0])
            if invalidProduct:
                break
        if not invalidProduct:
            filtered.append(product)                    
    return filtered

def checkProduct(products:list, locks:list):
    validProducts = []
    for product in products:
        invalidProduct = False
        validProducts.append([])
        for l, lock in enumerate(product):
            rotation = checkCombination(lock, locks[l])
            if rotation == []:
                invalidProduct = True
                break
            else:
                validProducts[-1].append(rotation)
        if invalidProduct:
            validProducts.pop(-1)

    return validProducts

def checkCombination(combination:list, lock:list):
    rotations = []
    for pick in combination:
        rotations.append(newMatchPickToLock(lock, pick))
    
    cartesianRots = cartesianProduct(rotations)
    for rotation in cartesianRots:
        ticks = []
        invalidRotation = False
        for pick in rotation:
            for tick in pick[1]:
                if tick not in ticks:
                    ticks.append(tick)
                else:
                    invalidRotation = True
                    break
            if invalidRotation:
                break
        if all(tick in ticks for tick in lock):
            return rotation
    return []


                

def main():
    if True:
        novicePicks = [
            [0,4,18],
            [0,12],
            [0,2],
            [0,10]
        ]

        noviceLocks = [
            [0,8,10,12,26],
            [12,24,28,30]
        ]

        advancedPicks = [
            [0,18],
            [0,14,16,18],
            [0,4,8],
            [0,8,18,22],
            [0,16],
            [0,12,16]
        ]

        advancedLocks = [
            [2,4,6,12,20,24,28],
            [2,10,18,28]
        ]

        expertPicks = [
            [0,22,24],
            [0,14],
            [0,14],
            [0,10],
            [0,2,12],
            [0,2],
            [0,10,14,24],
            [0,14],
            [0]
        ]

        expertLocks = [
            [2,6,10,20,24,28],
            [2,8,22],
            [4,6,8,14,22]
        ]

        masterPicks = [
            [4,6,8,24],
            [8,10,18,26],
            [24,26],
            [4,10,16,28],
            [0],
            [0],
            [0,18],
            [10,16],
            [2,8,12],
            [0],
            [2,8,12,14],
            [8,14,20]
        ]

        masterLocks = [
            [4,10,30],
            [4,10,16,24,28],
            [0,4,6,8,10,12,30],
            [0,8,12,22,24,30]
        ]

    customPicks = [
        [2,14],
        [10,12,24],
        [16,26],
        [2,18,28],
        [2,14,18,22],
        [2,4,12,20],
        [4,8,22],
        [10,24],
        [0,4,26],
        [6,10,26],
        [4,20,26],
        [4,6,18]
    ]

    customLocks = [
        [2,4,14,18,22,24],
        [2,4,12,16,30],
        [4,6,12,16,18,20,28],
        [0,2,6,16,18,22,30]
    ]

    picks = customPicks
    locks = customLocks

    picks = fixPicks(picks)

    combinedPicks = combinePicks(picks)

    writeList("combinePicks.txt", combinedPicks)

    lengths = []
    for comb in combinedPicks:
        lengths.append(f"length : {countCombTicks(comb)}\ncomb   : {comb}\n\n")
    
    writeList("lengths.txt", lengths)

    validCombs = filterCombinations(combinedPicks, locks)

    writeList("validCombs.txt", validCombs)

    cartesian = cartesianProduct(validCombs)
    writeList("cartesian.txt", cartesian)

    filtered = filterCartesian(cartesian, locks)
    writeList("filtered.txt", filtered)

    validProducts = checkProduct(filtered, locks)
    writeList("validProducts.txt", validProducts)



if __name__ == "__main__":
    t_start = time.time()
    main()
    t_end = time.time()
    print("Time taken: {:.6f}s".format(t_end - t_start))
