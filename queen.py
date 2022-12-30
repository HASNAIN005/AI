import time

numqueens = 4
currentsolution = [0 for x in range(numqueens)]
solution = []


def isafe(testrow, testcol):
    if testrow == 0:
        return True
    for row in range(0, testrow):

        if testcol == currentsolution[row]:
            return False

        if abs(testrow - row) == abs(testcol - currentsolution[row]):
            return False

    return True


def placequeens(row):
    global numqueens, currentsolution, solution

    for col in range(numqueens):
        if not isafe(row, col):
            continue
        else:
            currentsolution[row] = col
            if row == (numqueens - 1):
                solution.append(currentsolution.copy())
            else:
                placequeens(row + 1)



time.sleep(2)
placequeens(0)

print(len(solution), "solutions found")

for x in solution:
    print(x)
