# List is a ordered and changeable.Allows duplicate members.Syntax = []

arr = [5,[99,88],6,12.9,19,7]
# print(type(arr))
# print(arr[1][0])
# print(arr[1][1])

Arr = [
    [8,5,9],
    [12,7,54],
    ['ABBAS',2.5,True,-1]
]
# for array in Arr:
#     for elements in array:
#         print(elements)

#Tuples is collection which is ordered and unchangeable.Allows duplicate members.Syntax = ()
tup = (5,99,6,12.9,99,7)
# print(type(tup))
# print(tup)
# tup[1] = 100    #Error: Bcz its unchangeable
# print(tup[1])
# for i in tup:
#     print(i)

# Set is a collection which is unordered, unchangeable and unindexed. No duplicate members allowed. Syntax = {}
a = {5,99,6,12.9,99,7,'xyz'}
# print(type(a))
# a[-1]= 'abc'   #Error: Bcz its unchangeable
# print(a)

# Dictionary is a collection which is ordered and changeable but no duplicate members. Syntax = { Key: value }
dic = {'Name':'Ali' ,'Age': 20 ,'Salary': 50000}
# print(type(dic))
# print(dic['Age'])     #We can GET values through keys
# for i in dic:
#     print(dic[i])

lst = [
{'Name':'Ali' ,'Age': 30 ,'Salary': 53000},
{'Name':'Hassan' ,'Age': 25 ,'Salary': 60000},
{'Name':'Zubair' ,'Age': 18 ,'Salary': 25000},
{'Name':'Saqlain' ,'Age': 22 ,'Salary': 58000}
]
for i in lst:
    for j in i:
        print(j,i[j])