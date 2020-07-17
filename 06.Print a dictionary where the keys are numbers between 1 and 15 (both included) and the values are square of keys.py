"""Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys	"""


d1={}
length = int(input("Enter the size of dictionary:"))
for i in range(0,length):
    key = int(input('Enter the key interger:'))
    d1[key] = key*key
print(d1)