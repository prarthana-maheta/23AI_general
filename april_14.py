# encapsulation--OOP--data hiding

# access specifiers

# public -- globally
# protected -- within the class,inhertitaed class 
# private -- within the class


# class A:
#     data = "data1" #public--globally
#     _data = "data2" #protected -- parital
#     __data = "data3" #private -- zero 

#     def _display(self):
#         return self.__data


# class B(A):
#     def display(self):
#         print(self._display())
#         # print(super().__data)
#         print(self.data)
#         print(self._data)
#         # print(self.__data)

# b = B()
# b.display()
# print(b.data)
# print(b._data)



# polymorphism ----multiple ---action,method

# method overloading, method overridng

# class A:

#     def display(self,name):
#         print(name)

#     def display(self):
#         print("display A")

# # class B(A):
# #     def display(self):
# #         print("display B")

# a =A()
# a.display('name')



# abstraction

# from abc import ABC,abstractmethod
# # # import abc

# class AbstractCl(ABC):

#     def display(self):
#         print("abc")

#     @abstractmethod
#     def abcdisplay(self,a):
#         pass

# class Child(AbstractCl):
#     def abcdisplay(self):
#         print("abc display")
#     pass

# ch = Child()
# ch.abcdisplay()


# OOP-class,objects-inheri-poly-encap-abstract

# advance functions



# lambda


# map()
# reduce()
# filter()
# lambda


# dict collection modules

# exception handling
# file operation

# packages modules
# json
# requests
# time, datetime,random,regex
