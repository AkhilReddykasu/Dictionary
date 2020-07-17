"""Print each item and its corresponding type from the following list."""


d1 = {'akhil' : 'kasu' ,'ayan' : 95 , 'bala' : 25.4 }
d1['asha'] ='nikhil'
print(d1)
print("Prints each item and its corresponding type from the following list:")
for i in d1:
    print(i,type(d1[i]))