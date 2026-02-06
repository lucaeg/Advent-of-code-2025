import numpy as np
from functools import cache

# read and parse data
with open("day7.txt", "r") as f:
    matrix = [list(line) for line in f.read().splitlines()[1:]]

numRows = len(matrix)
numCols = len(matrix[0])

# fill in the light rays
for i in range(numRows):
    for j in range(numCols):
        if matrix[i][j] == "^":
            matrix[i][j - 1] = "|"
            matrix[i][j + 1] = "|"
        if i > 0 and matrix[i - 1][j] == "|" and matrix[i][j] == ".":
            matrix[i][j] = "|"

# Put in "x" on boundaries
transpose = np.array(matrix).T
for j in range(numCols):
    index = np.where(transpose[j] == "|")
    if matrix[index[0][0] - 2][j] != "^":
        matrix[index[0][0] - 1][j] = "x"


# function for counting the number of light ray paths
# cache for speedup
@cache
def find_num_paths(i, j):
    result = 0
    # Local copies for itteration
    ii, jj = i, j
    while matrix[ii][jj] == "|":
        if (
            matrix[ii][jj - 1] == "^"
            and matrix[ii - 1][jj] == "|"
            and matrix[ii - 1][jj - 1] == "|"
        ):
            result += find_num_paths(ii - 1, jj - 1)
        if (
            matrix[ii][jj + 1] == "^"
            and matrix[ii - 1][jj] == "|"
            and matrix[ii - 1][jj + 1] == "|"
        ):
            result += find_num_paths(ii - 1, jj + 1)
        ii = ii - 1

    if matrix[ii][jj] == ".":
        if matrix[ii + 1][jj - 1] == "^":
            result += find_num_paths(ii, jj - 1)
        if matrix[ii + 1][jj + 1] == "^":
            result += find_num_paths(ii, jj + 1)
    elif matrix[ii][jj] == "x":
        result += 1
    return result


# initiate the recursive path finding
numpaths = 2
for j in range(1, numCols - 1):
    if matrix[numRows - 1][j] == "|":
        numpaths += find_num_paths(numRows - 1, j)

print(numpaths)
