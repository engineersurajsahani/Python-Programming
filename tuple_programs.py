# insert update delete search count sort 

# Tuple Programs

l=tuple()
l=list(l)
l.append(11)
l.append(33)
print(l)
l.insert(1,22)
print(l)
l.insert(1,44)
print(l)
l[1]=99
print(l)
l.remove(22)
print(l)
l.remove(99)
print(l)
l.append(22)
l.append(44)
l.append(55)
l.append(66)
l.append(77)
l.append(88)
l.append(99)
print(l)
print(l.index(99))
l.append(11)
l.append(11)
l.append(11)
l.append(11)
l.append(11)
l.append(11)
if not l.index(99):
    print("99 is not present in the given list")
else:
    print("99 is present in the given list")
    
print("Count of element 11 :",l.count(11))
l.sort(reverse=True)
print(l)
