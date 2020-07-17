"""Remove duplicates from Dictionary"""
"""Removing duplicate values"""

d = {'jack sparrow': 'pirate',
     'will Turner': 'Elizabeth',
     'hendry Turner': 'will Turner',
     'Hector Barbossa': 'pirate'}
print("before removing duplicate values:\n",d)
d1 = {}
for k in d.keys():
    if d[k] not in d1.values():
        d1[k] = d[k]
print("After removing the duplicate values:\n",d1)











