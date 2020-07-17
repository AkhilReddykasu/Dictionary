"""Sum all the items in a dictionary"""
from typing import Dict

d: Dict[int, int] ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
print("Sum of values in dictionary:",sum(d.values()))
print("Sum of key in dict:",sum(d.keys()))

x= sum(d.values())
y = sum(d.keys())
print("Sum of dict keys and values:",x+y)



