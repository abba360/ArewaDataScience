### Day 4: 30 Days of python programming
## Exercise: Level 1
# Question 1
print('Thirty ' + 'Days ' + 'Of ' + ' Python')

# Question 2
print('Coding' + 'For' + 'All')

# Question 3
company = "Coding For All"

# Question 4
print(company)

# Question 5
print(len(company))

# Question 6
print(company.upper())

# Question 7
print(company.lower())

# Question 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Question 9
print(company[6:])

# Question 10
print(company.index("Coding")) #print it's index if True
print(company.find("Coding")) #print it's index if True
print(company.count("Coding")) #print the number of "Coding" found in the Company if True

# Question 11
print(company.replace("Coding","Python"))

# Question 12
print("Python for Everyone".replace("Everyone","All"))

# Question 13
print(company.split(" "))

# Question 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

# Question 15
print(company[0]) # C

# Question 16
print(company[13]) # l
print(company[-1]) # l

# Question 17
print(company[10]) # print space ' '

# Question 18
print(''.join(x[0] for x in 'Python For Everyone'.split()))

# Question 19
print(''.join(x[0] for x in company.split()))

# Question 20
print(company.find("C")) # 0

# Question 21
print(company.find("F")) # 7

# Question 22
print(company.rfind("l")) # 13

# Question 23
print( 'You cannot end a sentence with because because because is a conjunction'.find('because')) # the first index of "because" is 31
print( 'You cannot end a sentence with because because because is a conjunction'.index('because')) # the 1st index of "because" is 31

# Question 24
print( 'You cannot end a sentence with because because because is a conjunction'.rindex('because')) # returns the last index of "because" 47

# Question 25
print('You cannot end a sentence with because because because is a conjunction'.replace("because because because", "because"))

# Question 26
print('You cannot end a sentence with because because because is a conjunction'.find('because')) # returns the last index of "because" 47

# Question 27
print('You cannot end a sentence with because because because is a conjunction'.replace("because because because ", ""))

# Question 28
print(company.startswith("Coding")) # True

# Question 29
print(company.endswith("coding")) # False

# Question 30
print('   Coding For All      '.strip()) # Return's 'Coding For All'

# Question 31
print("30DaysOfPython".isidentifier()) # print False 
print("thirty_days_of_python".isidentifier()) # print True

# Question 32
print("# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# Question 33
print("I am enjoying this challenge. \nI just wonder what is next.")

# Question 34
print("Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki") 

# Question 35
radius = 10
area_of_circle = 3.14 * (radius**2)
"The area of a circle with radius {} is {} meters square.".format(radius,int(area_of_circle))

# Question 36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


