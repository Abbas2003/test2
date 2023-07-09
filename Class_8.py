# myData = { 'RgNo':1,'StdName':'M.Abbas','Age':20 }
# print(myData)
# print(type(myData))
# myData['StdName'] = 'Asad'
# myData['Age'] = 22
# print(myData)
# myData = { 'RgNo':1,'StdName':['M.Abbas','Asad','Aftab'],'Age':20 }
# print(myData['StdName'])
# for i in myData:
#     # print(myData[i])
#     print(i,myData[i])

myData =[ { 'RgNo':1,'StdName':'M.Abbas','Age':20 },
          { 'RgNo':2,'StdName':'Sakina','Age':19 },
          { 'RgNo':3,'StdName':'Asad','Age':21 },
          { 'RgNo':4,'StdName':'Adeel','Age':25 }
              ]
# print(myData)
# print(myData[1])
# print(type(myData))

# for i in myData:
#     print(i)

# for i in myData:
#     for j in i:
#         print(j,i[j])
#     print()

# abc = { 'RgNo':4,'StdName':'Adeel','Age':25 }
# abc.clear()
# abc.pop('StdName')
# print(abc)
# abc['sName'] = 'Hello Bhidu'
# print(abc)
# print(abc.popitem())

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# x = thisdict.values()
# print(x)
# for x,y in thisdict.items():
#     print(x,y)
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
#  }

# car.update({"year": 2020})
# print(car.values())
# x = car.keys()
# print(x) #before the change
#
# car["color"] = "white"
# print(x) #after the change

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
#
# for x,y in myfamily.items():
#     print(x,y)
           #Exception Handling
# try:
#     a=5
#     print(a)
#     print(1/0)
# # except NameError:
# #     print('Tunjho nalo chah ahye?')
# # except ZeroDivisionError:
# #     print('Nhi ho sakta yh bhai kiya kr rhe ho')
#
# except:  #It will handle all the errors
#  print('Errors jo masti ahye')

        #Assignment
# lst = []
# Dict = { }
# while True:
#     name = input("Enter your name: ")
#     Basic_sal = int(input("Enter Basic salary: "))
#     med_key = print('Medical Allowance')
#     Med_al = (Basic_sal*20)/100
#     Con_al = (Basic_sal*50)/100
#     Gross_sal = Basic_sal + Med_al + Con_al
#     Income_Tax = (Gross_sal*2)/100
#     Net_sal = Gross_sal - Income_Tax
#     Dict[name]=Basic_sal
#     Dict[med_key]=Med_al
#     break
# print(Dict)
# print(Med_al)
# print(Con_al)
# print(Gross_sal)
# print(Income_Tax)
# print(Net_sal)




