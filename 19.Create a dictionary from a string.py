"""Create a dictionary from a string"""
# 1

string1 = "{'jack sparrow': 'Captain pirate', 'will turner': 'Elizabeth', 'barbasoon': 'sailor'}"
d = eval(string1)
print("Create a dictionary from a string:\n", d)
print(d['jack sparrow'])

# 2

s1 = "'jack sparrow' - 'Captain pirate', 'will turner' - 'Elizabeth', 'barbasoon' - 'sailor'"
Dict = dict((x.strip(), y.strip())
            for x, y in (i.split('-')
                         for i in s1.split(', ')))
print("Creating a dict from string:\n",Dict)
print(d['will turner'])