"""Sort a dictionary by key	"""


import operator
d1 ={'tom' : 'jerry', 'mike' : 'tyson', 'jack' : 'ma', 'spaceX' : 'tesla'}
print("Dictionary before sorintg:\n",d1)
sort1 = dict(sorted(d1.items() , key = operator.itemgetter(0)))
print(sort1)


"""0 = sorting by key & 1 = sorting by value"""








