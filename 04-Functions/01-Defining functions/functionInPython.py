'''Functions in Python are reusable blocks of code designed to perform a specific task. They help in organizing code,
making it more readable,
and reducing redundancy.
'''


'''To define a function in Python, you use the def keyword, followed by the function name, 
parentheses (), and a colon :. '''

def function_name(parameters):
    """docstring"""
    statement(s)

def greet():
    """This function prints a greeting message."""
    print("Hello, welcome to Python functions!")

# Calling the function
greet()


#A function can be likened to a machine or appliance, like a washing machine.

def wash_clothes(clothes, detergent, settings):
    # Simulate the washing process
    return f"Washed {clothes} with {detergent} on {settings} settings"

# Calling the function
print(wash_clothes("shirts and pants", "liquid detergent", "normal"))
# Output: Washed shirts and pants with liquid detergent on normal settings
