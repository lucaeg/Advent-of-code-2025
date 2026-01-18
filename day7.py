import numpy as np
from functools import cache


def getMatrix():
    file1 = open("day7.txt", "r")
    lines = file1.readlines()

    matrix = []
    for line in lines[1:]:
        matrix.append(list(line.strip()))

    return matrix


matrix = getMatrix()
# Set global variables
numRows = len(matrix)
numCols = len(matrix[0])


def formatMatrix():
    i = 0
    j = 0
    while i < numRows:
        j = 0
        while j < numCols:
            if matrix[i][j] == "^":
                matrix[i][j + 1] = "|"
                matrix[i][j - 1] = "|"
            if i > 0 and matrix[i - 1][j] == "|" and matrix[i][j] == ".":
                matrix[i][j] = "|"

            j += 1
        i += 1
    # Put in "x" on boundaries
    transpose = np.array(matrix).T
    for j in range(numCols):
        index = np.where(transpose[j] == "|")
        if matrix[index[0][0] - 2][j] != "^":
            matrix[index[0][0] - 1][j] = "x"


formatMatrix()


# No caching, too slow
def find_num_paths(i, j):
    while matrix[i][j] == "|":
        if (
            matrix[i][j - 1] == "^"
            and matrix[i - 1][j] == "|"
            and matrix[i - 1][j - 1] == "|"
        ):
            find_num_paths(i - 1, j - 1)
        if (
            matrix[i][j + 1] == "^"
            and matrix[i - 1][j] == "|"
            and matrix[i - 1][j + 1] == "|"
        ):
            find_num_paths(i - 1, j + 1)
        i = i - 1
    if matrix[i][j] == ".":
        if matrix[i + 1][j - 1] == "^":
            find_num_paths(i, j - 1)
        if matrix[i + 1][j + 1] == "^":
            find_num_paths(i, j + 1)
    elif matrix[i][j] == "x":
        global numpaths
        numpaths += 1
        return


# Caching for performance
@cache
def find_num_paths_cache(i, j):
    result = 0
    # Local copies for itteration
    ii, jj = i, j
    while matrix[ii][jj] == "|":
        if (
            matrix[ii][jj - 1] == "^"
            and matrix[ii - 1][jj] == "|"
            and matrix[ii - 1][jj - 1] == "|"
        ):
            result += find_num_paths_cache(ii - 1, jj - 1)
        if (
            matrix[ii][jj + 1] == "^"
            and matrix[ii - 1][jj] == "|"
            and matrix[ii - 1][jj + 1] == "|"
        ):
            result += find_num_paths_cache(ii - 1, jj + 1)
        ii = ii - 1

    if matrix[ii][jj] == ".":
        if matrix[ii + 1][jj - 1] == "^":
            result += find_num_paths_cache(ii, jj - 1)
        if matrix[ii + 1][jj + 1] == "^":
            result += find_num_paths_cache(ii, jj + 1)
    elif matrix[ii][jj] == "x":
        result += 1
    return result


numpaths = 2
for j in range(1, numCols - 1):
    if matrix[numRows - 1][j] == "|":
        res = find_num_paths_cache(numRows - 1, j)
        numpaths += res

print(numpaths)
