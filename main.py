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
        f.write("\t%s\n" % obj)
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
        
def findPicksForLocks(picks:list, locks:list):
    picksForLocks = []
    for lock in locks:
        picksForLocks.append([])
        for pick in picks:
            picksForLocks[-1].append(matchPickToLock(pick, lock))
    return picksForLocks

def findLocksForPicks(picks:list, locks:list):
    picksForLocks = findPicksForLocks(picks, locks)

    locksForPicks = []
    for i,lock in enumerate(locks):
        locksForPicks.append([])
        for j, pick in enumerate(picks):
            locksForPicks[-1].append([])
            for k, solution in enumerate(picksForLocks[i][j]):
                if solution != []:
                    locksForPicks[-1][-1].append([j,rotatePick(picks[j], solution)])
                else:
                    locksForPicks[-1][-1].append([])

    for lock in locksForPicks:
        lock = removeEmpty(lock)
    return locksForPicks
            
def printLocksForPicks(locksForPicks:list):
    for lock in locksForPicks:
        for i, pick in enumerate(lock):
            print(f"{i+1} : {pick}")
        print("\n\n")

def checkCombination(combination:list, lock:list):
    mergedCombination = []
    for pick in combination:
        mergedCombination = mergedCombination + pick
    
    print(mergedCombination)
    if len(set(mergedCombination)) != len(mergedCombination):
        return False
    elif set(mergedCombination) != set(lock):
        return False
    return True

def powerSet(s:list):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def combineLocksForPicks(locksForPicks:list):
    combinations = []
    for lock in locksForPicks:
        for i, pick in enumerate(lock):
            if pick == []:
                lock.remove(pick)
            elif len(pick) == 1:
                continue
            else:
                continue
        combinations.append(powerSet(lock))
    
    filteredComb = []

    for lock in combinations:
        filteredComb.append([])
        for comb in lock:
            if comb != ():
                filteredComb[-1].append(list(comb))
    return filteredComb

def fixMultipleRotations(combinations:list):
    isChanged = True
    while isChanged:
        isChanged = False
        print("DÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\nDÖN BABA DÖNELİM\n")
        for l, lock in enumerate(combinations):
            for c, combination in enumerate(lock):
                print(len(lock))
                for p, pick in enumerate(combination):
                    if len(pick) > 1:
                        for r, rotation in enumerate(pick):
                            lock.append(combination[:p] + [[rotation]] + combination[p+1:])
                            isChanged = True
                        try:
                            lock.remove(combination)
                        except:
                            pass
    return combinations

def filterCombinations(locks:list, combinations:list):
    validCombinations = []
    for lock in locks:
        lockSet = set(lock)
        validCombinations.append([])
        for l, cLock in enumerate(combinations):
            for c, combination in enumerate(cLock):
                tickComb = []
                for pick in combination:
                    for tick in pick[0][1]:
                        tickComb.append(tick)
                if len(set(tickComb)) != len(tickComb):
                    continue
                elif set(tickComb) != set(lock):
                    continue
                else:
                    validCombinations[-1].append(combination)
    return validCombinations
                        
def combineLockSolutions(filteredCombinations:list):
    return itertools.product(filteredCombinations[:])


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



    picks = expertPicks
    locks = expertLocks

    l4p = findLocksForPicks(picks, locks)
    writeList("locksForPicks.txt", l4p)
    print("Locks for picks done")

    cl4p = combineLocksForPicks(l4p)
    writeNestedList("combineLocksForPicks.txt", cl4p)
    print("Combine locks for picks done")

    rotations = fixMultipleRotations(cl4p)
    writeList("rotations.txt", rotations)
    print("Fix multiple rotations done")

    filteredCombinations = filterCombinations(locks, rotations)
    writeList("filteredCombinations.txt", filteredCombinations)
    print("Filter combinations done")

    solutions = combineLockSolutions(filteredCombinations)
    writeList("solutions.txt", solutions)
    print("Combine solutions done")

if __name__ == "__main__":
    t_start = time.time()
    main()
    t_end = time.time()
    print("Time taken: {:.6f}s".format(t_end - t_start))
