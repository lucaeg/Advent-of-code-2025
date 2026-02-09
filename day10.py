import numpy as np
import scipy as sp

button_lists = []
target_buttons = []

# read and parse data
with open("day10.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        target_buttons.append(list(map(int, parts[-1][1:-1].split(","))))
        button_lists.append([list(map(int, b[1:-1].split(","))) for b in parts[1:-1]])


# represent buttons as spanning vectors
spanning_vectors = [
    np.array(
        [[1 if indx in b else 0 for indx in range(len(target_button))] for b in buttons]
    ).T
    for target_button, buttons in zip(target_buttons, button_lists)
]

# solve linear integer program to find a minimal
# combination of buttons to reach target button
ans = 0
for A, b in zip(spanning_vectors, target_buttons):
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

def pair_buttons(a, b):
    c = Counter(a + b)
    res = [int(k) for k, v in c.items() if v == 1 and k.isdigit()]
    return tuple(sorted(res))

def join_buttons(buttons1, buttons2):
    res = set()
    for a, b in itertools.product(buttons1, buttons2):
        joined = pair_buttons(a, b)
        if joined:
            res.add(joined)
    return list(res)

ans = 0
for i, target in enumerate(target_buttons):
    configurations = [tuple(b) for b in buttons[i]]
    if tuple(target) in configurations:
        ans += 1
        continue

    counter = 1
    while tuple(target) not in configurations:
        configurations = join_buttons(configurations, buttons[i])
        counter += 1

    ans += counter

print(ans)
"""
