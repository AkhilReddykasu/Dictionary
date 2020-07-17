"""To get the key, value and item in a dictionary"""

d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("key    value    count")
for i, (key, value) in enumerate(d.items(), 0):
    print(key, '    ', value, '    ', i)
