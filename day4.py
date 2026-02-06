# read data
with open("day4.txt", "r") as f:
    lines = f.read().splitlines()
    input = [list(line) for line in lines]

line_number = len(input)
char_number = len(input[0])


# function to count the number of neighbors equal to '@'
def count_neighbors(input, i, j):
    nb_count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = i + dr, j + dc
            if 0 <= nr < line_number and 0 <= nc < char_number:
                if input[nr][nc] == "@":
                    nb_count += 1
    return nb_count


# count the total number of removable "@"
# we do this by repeatedly removing any removable "@" cells
# until no more can be removed
total_count = 0
removed_count = 1  # initialize

while removed_count != 0:
    removed_count = 0
    for i in range(line_number):
        for j in range(char_number):
            cell = input[i][j]
            if cell == ".":
                continue
            elif count_neighbors(input, i, j) < 4:
                # condition for removing is valid
                input[i][j] = "."
                removed_count += 1
    total_count += removed_count

print(total_count)
