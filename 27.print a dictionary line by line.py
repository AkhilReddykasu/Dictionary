"""print a dictionary line by line"""

d = dict(Tom='Jerry', mike='Tyson', Jack='pirate')
print('Printing a dictionary line by line:')
for k,v in d.items():
    print('key:', k,'value:', v)