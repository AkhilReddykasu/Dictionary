"""Multiply all the items in a dictionary"""

d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
val = 1
for i, j in d.items():
    val *= i * j
print("After multiplying all items in dict:", val)
