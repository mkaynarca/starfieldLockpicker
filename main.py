import time
from itertools import chain, combinations
import copy

def writeList(path2file:str, objs:list):
    f = open(path2file, "w", newline='', encoding='utf-8')
    for obj in objs:
        f.write("%s\n" % obj)
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
        combinations.append(powerSet(lock))

    for lock in combinations:
        for combination in lock:
            
    return combinations


def main():
    picks = [
        [0,4,18],
        [0,12],
        [0,2],
        [0,10]
    ]

    locks = [
        [0,8,10,12,26],
        [12,24,28,30]
    ]

    # picks = [
    #     [4,6,8,24],
    #     [8,10,18,26],
    #     [24,26],
    #     [4,10,16,28],
    #     [0],
    #     [0],
    #     [0,18],
    #     [10,16],
    #     [2,8,12],
    #     [0],
    #     [2,8,12,14],
    #     [8,14,20]
    # ]

    # locks = [
    #     [4,10,30],
    #     [4,10,16,24,28],
    #     [0,4,6,8,10,12,30],
    #     [0,8,12,22,24,30]
    # ]

    l4p = findLocksForPicks(picks, locks)

    cl4p = combineLocksForPicks(l4p)

    writeList("log.txt", cl4p)

if __name__ == "__main__":
    t_start = time.time()
    main()
    t_end = time.time()
    print("Time taken: {:.6f}s".format(t_end - t_start))
