"""Check multiple keys exists in a dictionary"""

d = {'Tom' : 'Jerry' ,
     'mike' : 'Tyson',
     'Jack' : 'pirate'}
print(d.keys() >= {'Tom','mike'})
print(d.keys() <= {'Tom' , 'Jack'})


s1 = set(['Jack', 'mike'])
s2 = set(['mike','sparrow'])
print(s1.issubset(d.keys()))
print(s2.issubset(d.keys()))
