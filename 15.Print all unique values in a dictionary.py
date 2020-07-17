"""Print all unique values in a dictionary"""

d = {'jack sparrow': 'pirate',
     'will Turner': 'Elizabeth',
     'hendry Turner': 'will Turner',
     'Hector Barbossa': 'pirate'}
print("before print all unique values in a dictionary:\n",d)
d1 = {}
for k in d.keys():
    if d[k] not in d1.values():
        d1[k] = d[k]
print("Printing unique values in a dictionary:\n",d1.values())








