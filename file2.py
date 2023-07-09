# print("My file 2")
# print("Bye"*2)
# x='3'
# print(type(x))
# y=3
# print(type(x))
# print(x,y)

# a=5
# b=4
# print(a,b)
# Swipe method1
# c=a
# a=b
# b=c
# Swipe method2
# a=a+b
# b=a-b
# a=a-b
# Swipe method3
# a,b=b,a
# print(a,b)


# print('Hello '+input("Enter your name "))
# print(input("enter your age: "))

# a = input("Enter text: ")
# print(type(a))
# a = int(a)
# print(type(a))

# Assignment#1
print("Employee Salary Dashboard")
print("-------------------------\n")
name = input("Enter your name: ")
basic_sal = int(input("Enter your basic salary: "))
print("\nEmployee name: ", name)
print("Basic salary : ", basic_sal)

# calculating gross sal
print("*********************")
medical = (50*basic_sal)/100
print("Medical allowances: ", medical)
uniform = (1000)
print("Uniform allowances: ", uniform)
convence = ((25*basic_sal)/100)
print("Convence allowances: ", convence)

# calculating net sal
print("*********************")
gross_sal = basic_sal + medical + uniform + convence
print("Gross Salary ", gross_sal)
print("*********************")
income_tax = (gross_sal*2)/100
print("2% Income Tax: ", income_tax)
print("*********************")
net_sal = gross_sal - income_tax
print("Your Net salary is: ", net_sal)