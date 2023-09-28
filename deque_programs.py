# Deque Programs

from collections import deque 

q=deque()
print(q)

# Add 
 
q.append(11)
q.append(22)
q.append(11)
q.append(22)
q.append(11)
q.append(22)
print(q)
q.appendleft(33)
q.appendleft(44)
q.appendleft(55)
print(q)
q.insert(2,100)
q.insert(3,200)
print(q)

# Delete
 
q.pop()
print(q)
q.popleft()
print(q)
q.remove(100)
print(q)

# Get

print(q[0])
print(q[-1])

# Count

print("Count of element 200 :",q.count(200))

# Size

print(len(q))

# Sort

q.reverse()
print(q)

# Rotate

q.rotate(2)
print(q)
q.rotate(-2)
print(q)

from collections import Counter
print(Counter(q))
