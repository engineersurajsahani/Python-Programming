from collections import defaultdict

def default_value():
    return 0
    
d=defaultdict(default_value)

print(d['Q'])
print(d['A'])
print(d['E'])

print(d.keys())
print(d.values())
print(d.items())

for index,key in enumerate(d):
    print(index," : ",key," : ",d[key])
