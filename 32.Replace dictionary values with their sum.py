"""Replace dictionary values with their sum"""


d = {1 : 1 ,2 : 4 , 3: 9, 4: 16 ,5 : 25}
sum = 0
for i in d.values():
    sum +=i
for k in d.keys():
    d[k] = sum
print(d)
