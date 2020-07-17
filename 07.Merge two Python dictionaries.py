"""Merge two Python dictionaries"""


d1 = {5: 25, 4: 16}
d2 = {7: 49, 8: 64, 9: 81, 6: 36, 2: 4}
d3 = d1.update(d2)
print(d1)