"""Count the values associated with key in a dictionary"""


d= {1: '', 2: 4, 3: '', 4: 16, 5: 25}
count = 0
for k,v in d.items():
    if v == '':
        pass
    else:
        count +=1

print("Number of values associated with values:",count)


