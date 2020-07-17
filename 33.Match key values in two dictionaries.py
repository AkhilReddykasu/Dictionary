"""Match key values in two dictionaries"""

d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
d2 = {6: 36, 7: 41, 5: 25, 8: 64, 3: 9}
d3= {}
for (k , v) in (d1.items() & d2.items()):
    d3[k] = v

print("Matching key and values in d1 and d2:\n",d3)



