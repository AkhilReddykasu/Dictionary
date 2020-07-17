"""Sort a list alphabetically in a dictionary"""
'''

d = { 'l2': ['b','e','h','i','g'],
      'l1': ['j', 'm','c','z','d'],
      'l4': ['u', 't','x','o','p'],
      'l3': ['y','q','v','k','d']
}

sorted_d ={}
for k, v in d.items():
      sorted_d[k] = sorted(v)
print("sort a list alphabetically in a dictionary:\n",dict(sorted(sorted_d.items())))



'''


l1 = [8 , 86, 824, 1, 978, 65]

new_li = sorted(l1)
print("Second highest ele in list:",new_li[-2])

length = len(l1)
for i in (0,length):
      for j in range(0,i+1):
            if l1[i] > l1[j]:
                  temp = l1[i]
                  l1[i] = l1[j]
                  l1[j] = temp
print("second highest number:",l1[-2])
print(l1)


