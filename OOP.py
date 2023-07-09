# class MyClass:
#     a = 123
#     def __init__(self,myValue):
#         print('Start my class')
#         self.a = myValue
#
#     def myFun(self):
#         print(self.a)
#
#     def myFunction(self,v1=1,v2=1):
#         print('Hello i am a class function',self.a)
#         self.a = v1*v2
#         self.abc()
#
#     def abc(self):
#         print('HELL0 ABC')

# obj = MyClass('Boom')
# obj.a = 456
# print(obj.a)
# obj.myFunction(2,3)
# print(obj.a)
# obj.myFun()

# ___________________________________________________________________________________________________
#ENCAPSULATION
class encapsulation:
    __a = 321
    _b = 10
    def myFunction(self):
        self.__a = 'This is a private function'
        print(self.__a)
    def _myProtected(self):
        self._b = 'This is a protected method'
        print(self._b)

# obj = encapsulation()
# obj.myFunction()
# obj._myProtected()

# ___________________________________________________________________________________________________
# INHERITANCE

class myClass:
    RgNo = 891
    def myFunction1(self):
        self.myFunction2()
        print('Hello I am a super-class function')

class MySubClass (myClass):
    def myFunction2(self):
        print('Hello I am a sub-class function')

# obj = MySubClass()
# obj.myFunction1()


# ___________________________________________________________________________________________________
#POLYMORPHISM
class A:
    def fun(self):
        print('Hello A')

class B(A):
    def fun797(self):
        print('Hello B')

class C(B):
    def fun000(self):
        print('Hello C')

# obj = C()
# obj.fun()

# ___________________________________________________________________________________________________
# ABSTRACT

from abc import ABC,abstractmethod

class abstract(ABC):
    @abstractmethod
    def fun1(self):
        pass

    def fun2(self):
        print('This is fun2')

class Sub_abstract(abstract):
    i = 1000
    def fun1(self):
        print('I am a child class ')

Sub_abstract().fun1()