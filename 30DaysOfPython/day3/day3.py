### Day 3: 30 Days of python programming
## Exercise: Level 1
# Question 1
age = 23

# Question 2
height = 18.5

# Question 3
complexVar = 1 - 1j

# Question 4
b = int(input("Enter base: "))
h = int(input("Enter height: "))
area = 0.5 * b * h
print(" The area of the triangle is ", area)

# Question 5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is 12",perimeter)

# Question 6
lenght = int(input("Enter lenght: "))
width = int(input("Enter width: "))
area = lenght * width
perimeter = 2 * ( lenght + width)

# Question 7
rad = int(input("Enter radius: "))
pi = 3.14
area_of_circle = pi * (rad**2)
circum_of_circle = 2 * pi * rad

# Question 8
x = 2
y = 2*x -2

# Question 9
m = 10-2 / 6-2

# Question 10
print(y == m)

# Question 11
x = int(input("Enter a num x: "))
y = x**2 + 6*x + 9

# Question 12
print(len("python") is len("dragon"))

# Question 13
print("dragon".find("on") is "python".find("on"))

# Question 14
print( "jargon" in "I hope this course is not full of jargon")

# Question 15
print("dragon".find("on") is not "python".find("on"))

# Question 16
str_python = str(float(len("python")))

# Question 17
#checks for even
if num % 2 == 0:
    print("even")
#checks for odd
else:
    print("odd")

# Question 18
print(type(7 // 3 ) == type(int(2.7)))
# Question 19
print(type("10")==type(10))

# Question 20

print(int("9.8")== 10)

# Question 21
hours = input("Enter hours: ")
rate_per_pay = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_pay
print("Your weekly earning is ",weekly_earning)

# Question 22
year = int(input("Enter number of years you have lived: "))
days = year * 365
hours = days * 24
months = hours * 60
sec = months * 60
print("Your weekly earning is ",sec)

# Question 23
num=1
for i in range(1,6):
    print(i,num,i,i*i,i*i*i)
