
"""
Program 2 : Write a python code using lambda to check every item of  a list
 is an integer or string ?

"""

data = [10, 'hello', 3.14, 'world', 42, True, 'Python']

# Function to check if an item is an integer or a string
check_type = lambda x: 'Integer' if isinstance(x, int) else 'String' if isinstance(x, str) else 'Other'

# Apply the function to each item in the list
result = map(check_type, data)

# Print the results
print(list(result))
