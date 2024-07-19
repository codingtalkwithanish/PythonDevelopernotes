'''Parameters and Arguments
Functions can take parameters (also called arguments) that provide inputs to the function.

Types of Parameters
Positional Parameters: Parameters that must be passed in the correct order.
Keyword Parameters: Parameters that are passed with a key=value syntax.
Default Parameters: Parameters that have default values if no value is provided.
Arbitrary Arguments: Parameters that can take any number of arguments
using *args for positional arguments and **kwargs for keyword arguments.
'''

def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Calling the function with positional arguments
print(add(5, 3))  # Output: 8

def greet(name, message="Hello"):
    """This function prints a greeting message with a name."""
    print(f"{message}, {name}!")

# Calling the function with a keyword argument
greet(name="Alice")  # Output: Hello, Alice!
greet(name="Bob", message="Hi")  # Output: Hi, Bob!

def fruits(*args):
    """This function prints a list of fruits."""
    for fruit in args:
        print(fruit)

# Calling the function with arbitrary arguments
fruits("Apple", "Banana", "Cherry")

def student_info(**kwargs):
    """This function prints student information."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with arbitrary keyword arguments
student_info(name="John", age=22, course="Physics")
