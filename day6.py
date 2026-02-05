import math

# read file and extract data
with open("day6.txt", "r") as f:
    lines = f.read().splitlines()

operations = lines[-1].split()
numbers = [list(line.replace(" ", "x")) for line in lines[:-1]]

# transpose to get elf number grid
elf_numbers_grid = list(zip(*numbers))


elf_numbers = []
temp_number_list = []

# create a list of the elf numbers
for col in elf_numbers_grid:
    if all(ch == "x" for ch in col):
        elf_numbers.append(temp_number_list)
        temp_number_list = []
        continue
    number = "".join(ch for ch in col if ch != "x")
    temp_number_list.append(number)
elf_numbers.append(temp_number_list)


# calculate result
res = 0
for op, numbers in zip(operations, elf_numbers):
    if op == "+":
        res += sum(list(map(int, numbers)))
    else:
        res += math.prod(list(map(int, numbers)))

print(res)
