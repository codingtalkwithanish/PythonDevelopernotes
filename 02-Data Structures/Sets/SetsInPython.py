'''A set is an unordered collection of unique elements. Sets are mutable,
but the elements contained in them must be immutable.
Sets are useful for performing mathematical set operations like union,
intersection, difference, and symmetric difference.'''

'''
You can create a set using curly braces {} or the set() function.
'''

# Using curly braces
my_set = {1, 2, 3, 4, 5}

# Using the set() function
my_set = set([1, 2, 3, 4, 5])

# Creating an empty set (note: {} creates an empty dictionary)
empty_set = set()

'''Accessing Elements
Sets are unordered, so you cannot access elements by index or slice. 
You can iterate over the elements in a set.'''

my_set = {1, 2, 3, 4, 5}

# Iterating through a set
for element in my_set:
    print(element)



#You can add elements to a set using the add() method and remove elements
# using the remove() or discard() methods.


my_set = {1, 2, 3}

# Adding elements

my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Removing elements
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Using discard (no error if element not found)
my_set.discard(5)
print(my_set)  # Output: {1, 3, 4}


# Using pop (removes and returns an arbitrary element)
popped_element = my_set.pop()
print(popped_element)
print(my_set)


# Clearing all elements
my_set.clear()
print(my_set)  # Output: set()


'''Set Operations
Sets support various mathematical operations like union, intersection, difference, 
and symmetric difference.'''


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {4, 5}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2, 3}

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}





#copy(): Returns a shallow copy of the set.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# copy()
set1 = {1, 2, 3}
set_copy = set1.copy()
print(set_copy)  # Output: {1, 2, 3}

#difference(*others): Returns the difference of the set and all others.
# difference()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.difference(set2))  # Output: {1, 2}


#difference_update(*others): Removes all elements of another set from this set.
# difference_update()
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

#discard(elem): Removes an element if it is a member.

# discard()
set1.discard(1)
print(set1)  # Output: {2}

#intersection(*others): Returns the intersection of the set and all others.

# intersection()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))  # Output: {3, 4}

#intersection_update(*others): Updates the set with the intersection of itself and others.

# intersection_update()
set1.intersection_update(set2)
print(set1)  # Output: {3, 4}

#isdisjoint(other): Returns True if two sets have a null intersection.

# isdisjoint()
set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True

#issubset(other): Returns True if another set contains this set.

# issubset()
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True

#issuperset(other): Returns True if this set contains another set.

# issuperset()
print(set2.issuperset(set1))  # Output: True


#pop(): Removes and returns an arbitrary element from the set.


# pop()
set1 = {1, 2, 3}
popped = set1.pop()
print(popped)  # Output: 1 (or any other element)
print(set1)

#remove(elem): Removes an element from the set. If the element is not a member, raises a KeyError.

# remove()
set1 = {1, 2, 3}
set1.remove(2)
print(set1)  # Output: {1, 3}

#symmetric_difference(other): Returns the symmetric difference of two sets.

# symmetric_difference()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}

#symmetric_difference_update(other): Updates the set with the symmetric difference of
# itself and another.

# symmetric_difference_update()
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 5, 6}


#union(*others): Returns the union of sets.

# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

#update(*others): Updates the set with the union of itself and others.


# update()
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}