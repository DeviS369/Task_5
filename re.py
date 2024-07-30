"""
Program 4 : Regular Expression


import re

# Email Address
email = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Mobile Numbers in Bangladesh

mobile_number = '^(?:\+880|0)1[3-9]\d{8}$'

#Telephone Numbers in the USA
tele_no_usa = '^(\(\d{3}\)\s?|\d{3}[-\s]?)\d{3}[-\s]?\d{4}$'

#To create a regular expression for a 16-character alphanumeric password 
# composed of uppercase letters, lowercase letters, special characters, 
# and numbers, you can use the following pattern

pwd = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
"""
