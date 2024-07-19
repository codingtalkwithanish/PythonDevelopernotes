'''Lambda functions are small anonymous functions defined with the lambda keyword.
They can have any number of arguments but only one expression
'''

#lambda arguments: expression

# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Using lambda functions with built-in functions
numbers = [1, 2, 3, 4, 5]

# Doubling each element using map()
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]

# Filtering even numbers using filter()
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]

# Sorting a list of tuples by the second element using sorted()
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]
