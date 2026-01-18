file1 = open("day3.txt", "r")
lines = file1.readlines()

res = 0
for line in lines:
    int_list = list(line)[:-1]
    res_str = ""

    for i in range(12):
        j = 11 - i
        index = len(int_list) - j
        max_element = max(int_list[:index])
        max_index = int_list.index(max_element)
        int_list = int_list[(max_index + 1) :]
        res_str += max_element

    res += int(res_str)

print(res)
