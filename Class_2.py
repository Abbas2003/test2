# print(9**2) #it means 9 ka square
# print(9//2) #it takes the first value before decimal(Whole number)
# print(9%4) #modulo operator(remainder)
# print(9/4)

# Relation Operators
# ==, <, >, <=, >=, !=
# Logical Operator
# (AND)(Both conditions check), (OR)(Any one condition check), (NOT)

# a = 2
# print(a)
# a += 3
# print(a)
# a -= 1
# print(a)
# a *= 2
# print(a)
#
# print(2==3)
# print(2<2)
# print(2>2)
# print(2<=2)
# print(2>=2)
# print(1!=1)
# print('iHi' != 'iHi')
# print('Two' != 'Two')
# print(True != False)
#
# print(True and True and True and False)
# print(True and True and True and True)
#
# print(False or True or False or False)
# print(not(True))

# a=1
# b=2
# print(not ((a+b) > 4) )
# print(not(a==b) and b!=a)
# print(not(a+b == 3) or (a==b))

# print("Start my program")
# if(False):
#     print('ABC')
# else:
#     print('XYZ')
# print("End my program")

# v1 = input("Enter user ID: ")
# v2 = input("Enter Password: ")
# if(v1 == 'abc' and v2 == '123'):
#     print("Successfull login")
# else:
#     print("Invalid ID or password")

          #Assignment 2
# m1=int(input("Enter marks of Maths: "))
# m2=int(input("Enter marks of English: "))
# m3=int(input("Enter marks of Physics: "))
# m4=int(input("Enter marks of Urdu: "))
# m5=int(input("Enter marks of Chemistry: "))
# sum=m1+m2+m3+m4+m5
# percentage=(sum*100)/500
# print(f'You got{percentage} %')
# if(percentage<30):
#     print("Grade: FAIL")
# elif(percentage>30 and percentage<50):
#     print("Grade: C")
# elif(percentage>50 and percentage<70):
#     print("Grsde: B")
# elif(percentage>70 and percentage<80):
#     print("Grade: A")
# elif(percentage>80 and percentage<99):
#     print("Grade: A+")
# else:
#     print("Invalid input")

#Factorial:
# x=int(input("Enter number to get factorial: "))
# factorial = 1
# if x < 0:
#     print("Factorial of negative numbers doesn't exist.")
# elif x == 0:
#     print("Facorial of 0 is 1.")
# else :
#     for i in range(1,x+1):
#         factorial = factorial*i
#     print(f'Factorial of {x} is {factorial}.')

#Assignment:
m = int(input("Enter marks of maths: "))
c = int(input("Enter marks of chemistry: "))
p = int(input("Enter marks of physics: "))
total = m+c+p
per = int((total * 100)/300)
print(per)
grade = ''
if(per > 90):
    grade = 'A'
elif(per > 80):
    grade = 'B'
elif(per > 70):
    grade = 'C'
else:
    grade = "Fail"

print(f'Grade: {grade}')

