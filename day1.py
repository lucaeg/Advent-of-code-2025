# read file and extract data
with open("day1.txt", "r") as f:
    lines = f.read().splitlines()

i = 50
password_counter = 0

for line in lines:
    val = int(line[1:])
    password_counter += val // 100
    val = val % 100
    if line[0] == "L":
        if val >= i and i != 0:
            password_counter += 1
        i = (i - val) % 100
    else:
        if val >= (100 - i):
            password_counter += 1
        i = (i + val) % 100

print(password_counter)
