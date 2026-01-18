import numpy as np
import scipy as sp

file1 = open("day10.txt", "r")
buttons = []
target_buttons = []
for line in file1.readlines():
    target = line.strip().split()[-1]
    target_button = list(map(int, target[1:-1].split(",")))
    target_buttons.append(target_button)
    button = line.strip().split()[1:-1]
    button_list = [list(map(int, b[1:-1].split(","))) for b in button]
    buttons.append([b for b in button_list])


def create_spanning_vectors():
    spanning_vectors = []
    for i in range(len(target_buttons)):
        basis = []
        dim = len(target_buttons[i])
        for b in buttons[i]:
            vector = [0 for j in range(dim)]
            for char in b:
                vector[char] = 1
            basis.append(vector)
        spanning_vectors.append(np.array(basis).T)
    return spanning_vectors


spanning_vectors = create_spanning_vectors()

ans = 0
for i in range(len(target_buttons)):
    A = spanning_vectors[i]
    b = np.array(target_buttons[i])
    constrains = sp.optimize.LinearConstraint(A, lb=b, ub=b)
    c = np.ones(len(A[0]))
    integrality = np.ones_like(c)

    coeffs = sp.optimize.milp(c=c, constraints=constrains, integrality=integrality).x
    ans += sum(coeffs)

print(ans)


"""
# Part one

import itertools
from collections import Counter

def pair_buttons(pair):
    a, b = pair
    c = Counter(a + b)
    res = list("".join(k for k, v in c.items() if v == 1 and k.isdigit()))
    res.sort()
    return res

def join_buttons(buttons1, buttons2):
    res = []
    for pair in itertools.product(buttons1, buttons2):
        joined_button = pair_buttons(pair)
        if joined_button != []:
            res.append(joined_button)
    return convert_to_regualar_tuples(list(set(tuple(x) for x in res)))


def convert_to_regualar_tuples(list):
    for i in range(len(list)):
        list[i] = tuple(map(int, list[i]))
    return list


ans = 0
for i in range(len(buttons)):
    configurations = buttons[i]
    if target_buttons[i] in [eval(conf) for conf in configurations]:
        ans += 1
        continue
    counter = 1
    while target_buttons[i] not in configurations:
        configurations = join_buttons(list(map(str, configurations)), buttons[i])
        counter += 1
    ans += counter

print(ans)
"""
