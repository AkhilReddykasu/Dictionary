"""Print a dictionary in table format"""

d = {'jack sparrow': 'pirate',
     'will Turner': 'Elizabeth',
     'hendry Turner': 'will Turner',
     'Hector Barbossa': 'pirate'}
print("keys                      values                     count")
for i, (k,v) in enumerate(d.items(),1):
    print(k,'               ',v,'                 ',i)



