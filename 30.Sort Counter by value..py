"""Sort Counter by value."""
import operator
d = {'a': 1 , 'c': 3, 'b': 2, 'z': 26, 'e': 5, 'y': 25}
sort = dict(sorted(d.items(), key = operator.itemgetter(1) ))
print("before sorting by keys:\n",d)
print("Sort counter by value:\n",sort)

"""0 = sorting by keys & 1 = sorting by values"""

from collections import Counter
d1 = {'tom': 'jerry',
     'mike tyson': 'boxer',
     'jack pirate': 'sparrow',
     'will Turner': 'Elizabeth'}

x = Counter(d1)
print('sorting by items:\n',sorted(d1.items()))
