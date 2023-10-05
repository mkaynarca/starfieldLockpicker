import time
import itertools

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
                    locksForPicks[-1][-1].append(rotatePick(picks[j], solution))
                else:
                    locksForPicks[-1][-1].append([])

    return locksForPicks
            

        

def main():
    # picks = [
    #     [0,4,18],
    #     [0,12],
    #     [0,2],
    #     [0,10]
    # ]

    # locks = [
    #     [0,8,10,12,26],
    #     [12,24,28,30]
    # ]

    picks = [
        [0,4,10],
        [0,8],
        [0,6,12,14],
        [0,12],
        [0,6,8,18],
        [0,4,12],
        [0,4,14]
    ]

    locks = [
        [0,2,6,10,16,24,30],
        [4,6,10,12,18]
    ]

    locksForPicks = findLocksForPicks(picks, locks)

if __name__ == "__main__":
    t_start = time.time()
    main()
    t_end = time.time()
    print("Time taken: {:.6f}s".format(t_end - t_start))
