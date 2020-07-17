"""Combine two dictionary adding values for common keys."""

d1 ={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
d2 ={4: 64, 8: 64, 9: 81, 2: 8}
d3 ={}
for k in d1.keys():
    if k in d2.keys():
        d3[k]= [d1[k],d2[k]]
    else:
        d3[k] = d1[k]
for key in d2.keys():
    if key not in d3.keys():
        d3[key] = d2[key]
print("combining two dictionaries and adding values for common keys:\n",d3)







