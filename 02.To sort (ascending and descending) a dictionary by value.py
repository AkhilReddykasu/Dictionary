'''To sort (ascending and descending) a dictionary by value'''

import operator
d1 = {'akhil': 'reddy', 'asha': 'nikhil', 'ayan': 'khan'}
print("Dictionary before sorting by value:\n",d1)
sort1 = dict(sorted(d1.items(), key = operator.itemgetter(1)))
print("Dictionary ascending order:\n",sort1)
sort2 = dict(sorted(d1.items(), key = operator.itemgetter(1), reverse=True))
print("Dictionary decending order by value:\n",sort2)

