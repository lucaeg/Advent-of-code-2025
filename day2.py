import textwrap

# read file and extract data
with open("day2.txt", "r") as f:
    ranges = f.readline().split(",")


# function to check if an id is valid
def is_valid(id):
    half_length = len(id) // 2

    for i in range(1, half_length + 1):
        if len(id) % i:
            continue
        # slice id into equal sized numbers
        numbers = list(textwrap.wrap(id, i))
        # check if all slices are equal
        if all(x == numbers[0] for x in numbers):
            return True
    return False


# count the valid ids
counter = 0
for interval in ranges:
    start, end = map(int, interval.split("-"))
    for id in range(start, end + 1):
        if is_valid(str(id)):
            counter += id

print(counter)
