'''Check if a given key already exists in a dictionary'''


d1 = {'bod': 'Jerry', 'Tom': 'Oogly', 'Chota bheem': 'Chutki', 'ben10': 'cartoon'}
key = input("Enter a key to find is in dictionary or not:")
if key in d1.keys():
    print("Given key already exists")
else:
    d1[key]=input("enter a value:")
    print(d1)
