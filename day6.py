import numpy as np
import math
import sys

np.set_printoptions(threshold=sys.maxsize)

file1 = open("day6.txt", "r")
lines = file1.readlines()
file1.close()

operations = lines[-1].split()

numbers = []
for line in lines[:-1]:
    char_list = list(line)[:-1]
    for i in range(len(char_list)):
        if char_list[i] == " ":
            char_list[i] = "x"
    numbers.append(char_list)

numbers = np.array(numbers)
elf_numbers_list = numbers.T


def all_equal_to_x(listen):
    count = 0
    for j in range(len(listen)):
        if listen[j] == "x":
            count += 1
    if count == len(listen):
        return True
    return False


elf_numbers = []
temp_number_list = []
for i in range(len(elf_numbers_list)):
    if all_equal_to_x(elf_numbers_list[i]):
        elf_numbers.append(temp_number_list)
        temp_number_list = []
        continue
    number = elf_numbers_list[i]
    filtered_number = "".join(list(filter(lambda a: a != "x", number)))
    temp_number_list.append(filtered_number)
elf_numbers.append(temp_number_list)

res = 0
for i in range(len(operations)):
    if operations[i] == "+":
        res += sum(list(map(int, elf_numbers[i])))
    else:
        res += math.prod(list(map(int, elf_numbers[i])))

print(res)
