# read file and extract data
with open("day3.txt", "r") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    res_str = ""

    for i in range(12):
        index = len(line) - (11 - i)
        max_element = max(line[:index])
        max_index = line.index(max_element)
        line = line[(max_index + 1) :]
        res_str += max_element

    res += int(res_str)

print(res)
