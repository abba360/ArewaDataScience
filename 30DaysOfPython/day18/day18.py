# What is the most frequent word in the following paragraph?
import re
regex_pattern = r'[(d{1,}|D{1,})].+'
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
matches = re.findall(regex_pattern, paragraph,re.I)

print(matches)


# Question 2
# The position of some particles on the horizontal x-axis are -12, -4, -3 
# and -1 in the negative direction, 0 at origin, 4 and 8 in the positive 
# direction. Extract these numbers from this whole text and find the 
# distance between the two furthest particles.
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12


# Exercises: Level 2
# Write a pattern which identifies if a string is a valid python variable
# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname')
def is_valid_variable(input):
    import re
    valid = re.findall(r'^[ab-zAB-z]', input,re.I)
    if valid :
        return True
    else:
        return False

print(is_valid_variable('abc-name')) # True
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # True
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

