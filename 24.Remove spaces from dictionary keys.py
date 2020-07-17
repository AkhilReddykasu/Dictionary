"""Remove spaces from dictionary keys"""

d = {'tom': 'jerry',
     'mike tyson': 'boxer',
     'jack pirate': 'sparrow',
     'will Turner': 'Elizabeth'}
print("Before removing spaces:\n", d)
d = {x.replace(' ', ''): v
     for x, v in d.items()}
print("After removing space:\n", d)




