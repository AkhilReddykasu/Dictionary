"""create a dictionary from two lists without losing duplicate values"""

from collections import defaultdict
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
temp = defaultdict(set)
for c, i in zip(class_list, id_list):
    temp[c].add(i)
print(temp)


li1 = ['jack ', 'tesla', 'Elon', 'Toyato']
li2 = ['sparrow', 'car', 'musk', 'car']
d ={}
length = len(li1)
for i in range(0,length):
    for j in range(0,i+1):
        d[li1[i]] = li2[j]

print("create a dictionary from two lists without losing duplicate values:\n",d)




