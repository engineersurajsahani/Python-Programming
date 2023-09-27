
# Create a List:

my_list = [1, 2, 3, 4, 5]

# Access an Element by Index:

my_list = [1, 2, 3, 4, 5]
print(my_list[2])  # Outputs: 3

# Add an Element to the List:

my_list = [1, 2, 3]
my_list.append(4)

# Remove an Element from the List:

my_list = [1, 2, 3]
my_list.remove(2)

# Iterate Over a List:

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# Find the Length of a List:

my_list = [1, 2, 3, 4, 5]
length = len(my_list)

# Check if an Element is in the List:

my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list")

# Concatenate Two Lists:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2

# Sort a List:

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()

# Reverse a List:

my_list = [1, 2, 3, 4, 5]
my_list.reverse()

# Count Occurrences of an Element in a List:

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = my_list.count(3)

# Find the Index of an Element in a List:

my_list = [10, 20, 30, 40, 50]
index = my_list.index(30)

# Slice a List:

my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]  # Returns [2, 3, 4]

# Copy a List:

original_list = [1, 2, 3]
copied_list = original_list.copy()

# Remove Duplicates from a List:

my_list = [1, 2, 2, 3, 3, 4, 4]
unique_list = list(set(my_list))

# Find the Maximum and Minimum Element in a List:

my_list = [4, 2, 9, 7, 5, 1]
max_value = max(my_list)
min_value = min(my_list)

# Add Two Lists Element-wise:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [x + y for x, y in zip(list1, list2)]

# Check if a List is Empty:

my_list = []
if not my_list:
    print("The list is empty")

# Find the Sum of All Elements in a List:

my_list = [1, 2, 3, 4, 5]
total = sum(my_list)

# Remove the Last Element from a List:

my_list = [1, 2, 3, 4, 5]
my_list.pop()