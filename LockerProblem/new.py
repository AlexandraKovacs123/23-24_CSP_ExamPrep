lockers = []

# Only worried about indexes from 1 - 100
def findPerfectSquares(max):
    max += 1
    for elem in range(max):
        lockers.append(0)

    for elem in range(max):
        lockers[elem] = 1

    for elem in range(max):
        if elem % 2 == 0:
            lockers[elem] = 0

    for student in range(3, max):
        for elem in range(max):
            if elem % student == 0:
                swapLocker(elem)


def prints():
    for locker in range(1, 101):
        if lockers[locker] == 1:
            print("Locker " + str(locker) + ": " + str(lockers[locker]))

def swapLocker(locker):
    if lockers[locker] == 0:
        lockers[locker] = 1
    else:
        lockers[locker] = 0



prints()