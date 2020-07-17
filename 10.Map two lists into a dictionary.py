"""Map two lists into a dictionary"""

l1 = ['Jack','Will Turner','Mike','Elizabeth']
l2 = ['pirate','black smith','boxer','Queen']
d={}
for i in range(0,len(l1)):
    for j in range(0,i+1):
        d[l1[i]] = l2[j]
print("Map two lists into a dictionary:\n",d)


new_d= dict(zip(l1,l2))
print("Map two lists into a dictionary:\n",new_d)


