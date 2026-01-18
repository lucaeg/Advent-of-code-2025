import numpy as np

file = open("day4.txt", "r")

input_raw = file.readlines()
line_number = len(input_raw)
char_number = len(input_raw[0].strip("\n"))

input = np.zeros((line_number, char_number), dtype=str)
for i in range(line_number):
    for j in range(char_number):
        input[i][j] = input_raw[i][j]

count = 0
grid_count = 1  # initialize

while grid_count != 0:
    grid_count = 0
    # Check midle grid
    for i in range(1, line_number - 1):
        for j in range(1, char_number - 1):
            cell_count = 0
            cell = input[i][j]
            if cell == ".":
                cell_count += 4
            if input[i - 1][j] == "@":
                cell_count += 1
            if input[i + 1][j] == "@":
                cell_count += 1
            if input[i][j - 1] == "@":
                cell_count += 1
            if input[i][j + 1] == "@":
                cell_count += 1
            if input[i - 1][j - 1] == "@":
                cell_count += 1
            if input[i - 1][j + 1] == "@":
                cell_count += 1
            if input[i + 1][j - 1] == "@":
                cell_count += 1
            if input[i + 1][j + 1] == "@":
                cell_count += 1
            if cell_count < 4:
                grid_count += 1
                input[i][j] = "."

    i = 0
    for j in range(1, char_number - 1):
        cell_count = 0
        cell = input[i][j]
        if cell == ".":
            cell_count += 4
        if input[i + 1][j] == "@":
            cell_count += 1
        if input[i][j - 1] == "@":
            cell_count += 1
        if input[i][j + 1] == "@":
            cell_count += 1
        if input[i + 1][j - 1] == "@":
            cell_count += 1
        if input[i + 1][j + 1] == "@":
            cell_count += 1
        if cell_count < 4:
            grid_count += 1
            input[i][j] = "."
    i = line_number - 1
    for j in range(1, char_number - 1):
        cell_count = 0
        cell = input[i][j]
        if cell == ".":
            cell_count += 4
        if input[i - 1][j] == "@":
            cell_count += 1
        if input[i][j - 1] == "@":
            cell_count += 1
        if input[i][j + 1] == "@":
            cell_count += 1
        if input[i - 1][j - 1] == "@":
            cell_count += 1
        if input[i - 1][j + 1] == "@":
            cell_count += 1
        if cell_count < 4:
            grid_count += 1
            input[i][j] = "."

    j = 0
    for i in range(1, line_number - 1):
        cell_count = 0
        cell = input[i][j]
        if cell == ".":
            cell_count += 4
        if input[i - 1][j] == "@":
            cell_count += 1
        if input[i + 1][j] == "@":
            cell_count += 1
        if input[i][j + 1] == "@":
            cell_count += 1
        if input[i - 1][j + 1] == "@":
            cell_count += 1
        if input[i + 1][j + 1] == "@":
            cell_count += 1
        if cell_count < 4:
            grid_count += 1
            input[i][j] = "."

    j = char_number - 1
    for i in range(1, line_number - 1):
        cell_count = 0
        cell = input[i][j]
        if cell == ".":
            cell_count += 4
        if input[i - 1][j] == "@":
            cell_count += 1
        if input[i + 1][j] == "@":
            cell_count += 1
        if input[i][j - 1] == "@":
            cell_count += 1
        if input[i - 1][j - 1] == "@":
            cell_count += 1
        if input[i + 1][j - 1] == "@":
            cell_count += 1
        if cell_count < 4:
            grid_count += 1
            input[i][j] = "."

    count += grid_count

corner = 1
count += corner

print(count)
