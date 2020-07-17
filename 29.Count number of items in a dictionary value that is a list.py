"""Count number of items in a dictionary value that is a list"""

d = {'a': 1, 'c': 3, 'b': 2, 'z': 26, 'e': 5, 'y': 25}
li1 = [2, 25, 5, 8, 9]
count = 0
for v in d.values():
    if v in li1:
        count += 1
print("Count number of items in a dictionary value that is a list:",count)




