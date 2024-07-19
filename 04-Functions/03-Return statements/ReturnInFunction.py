'''The return statement is used to exit a function and go back to the place
where it was called.
Optionally, a function can return a value or a set of values.'''

def multiply(a, b):
    """This function returns the product of two numbers."""
    return a * b

# Calling the function and storing the result in a variable
result = multiply(4, 5)
print(result)  # Output: 20

def calculate_area(radius):
    """This function returns the area and circumference of a circle."""
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

# Calling the function and unpacking the returned values
area, circumference = calculate_area(5)
print(f"Area: {area}, Circumference: {circumference}")
