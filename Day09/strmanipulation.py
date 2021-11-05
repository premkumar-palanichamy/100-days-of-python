# Splitting String

'''
Strings are represented as str objects.

Instance Methods:

Instance methods are the most common type of methods in Python classes. These are so called because they can access unique data of their instance.
(i.e) If you have two objects each created from a shape class, then they each shape may have different properties.
'''
import re

value = 'This is Prem'.split()
print(value)
#
whoami = "This is Prem"
value = whoami.split(' ')
print (value)

# Limiting the split with Maxsplit
s = "this is my string"
value = s.split(maxsplit=1)
print(value)

# Re-Split()

''' In general split doesnt not handle strings with multiple delimiters nor does it account for possible whitespace around delimiters. So thats were re.split() comes into picture'''
s = "this is prem!"
value = re.split(r'[!,\s]\s*',s)
print(value)

# Matching Text

''' To programmatically check the start or end of a string for specific text patterns'''

# -> To find the word start with http and it will print the boolean value (true or false)
s = 'http://www.google.com'
print(s.startswith('http'))

print(s.startswith('www.'))

print(s.endswith('com'))
print(s.endswith('.in'))

# Splitting a String using substring

s = "this is prem and basically from India"
print(s.split("and"))

# Note:

# '''
# # Avoid this:
# str.split('a,b,c', ',')
#
# # Do this instead:
# 'a,b,c'.split(',')
# '''