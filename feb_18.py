# functions
# def ai_batch_23():
#     pass
#     # return "heelo ai batch"
# print(ai_batch_23())
# def club_example():
#     # print("hello function") 
#     return "hello function"

# x=club_example()
# print(x)


# # parameters vs arguments
# def example(a,b):
#     print("example function is working")
#     print(a,b)
#     return a,b

# a,b=example("a","b")
# print(a,b)

# list1=['12','33','44','66'] --[12,33,44,66]
# tuple1=('66','77','88','99') --(66,77,88,99)

# # create a function that takes list1 and tuple1 as arguments,
# # convert each element from both into interger 
# # and return the updated list and tuple


# # def convert(list1,tuple1):
# #     l1=[]
# #     l2=[]
# #     for i in list1:
# #         l1.append(int(i))
# #     for j in tuple1:
# #         l2.append(int(j))
# #     return l1,tuple(l2)
# # print(list1)
# # print(tuple1)
# # l,t=convert(list1,tuple1)
# # print(l)
# # print(t)
# # arguments, parameters

# # 1) normal function
# # 2) parameterized functions
# # 3)default parameterized functions
# # 4)keyword arguments
# # 5) args 
# # 6)kwargs

# def example(a,b=0):
#     return a+b

# print(example(5,6))

# def example(first,second,third):
#     return first+second+third
# # print(example("hello","hii","heyy"))
# print(example(second="techno",first="royal",third="pvt ltd"))


# # arbitary arguments
# # *


# def example(a,b,*c):
#     print(a)
#     print(b)
#     print(c)
#     return a
# example(1,2,3,4,5,6)

# # list1[i] =33
# # [2,33,4,5,6,33,8,9,10,11]
# a,c=example(1,2,3,4,5,6,3,8,9,10,11)
# [1,2,33,4,5,6,33,8,9,10,11]




# def example(a,*b):
#     # print(b,a)
#     print(b)
#     c=list(b)
#     for i in range(len(c)):
#         if c[i] == 3:
#             c[i] = 33
#     return a,c
# a,c=example(1,2,3,4,5,6,7,3,8,9,10,11)
# list1=[]
# list1.append(a)
# list1.extend(c)
# print(list1)


# # kwargs
# # keyword arbitary args

def examlpe(*a,**c):
    print(c)
    print(a)
examlpe(1,2,4,5,6,78,apple="red",banana="yellow")

# Real Python Is Great !
'RealPythonIsGreat!'

# # def example(**data):
# #     # pass
# #     print(data)
# #     str1=""
# #     # for i in data.values():
# #     #     str1+=i
# #     return str1.join(data.values())

# # print(example(a="Real",b="Python",c="Is",d="Great",e="!"))


# decorators

# function in function
# def check1(func):
#     def inner(a,b):
#         print("in decorator")
#         if a > 0 and b > 0:
#             func(a,b)
#     return inner
# @check1
# def mul1(c,d):
#     print("in sum")
#     print(c*d)
# mul1(1,2)


# def make_pretty(funcion1):

#     def inner():
#         print("I got decorated")
#         funcion1()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()




def factorial_decorator(func):
    def inner(n):
        if n < 0:
            return 1
        elif n == 0 or n == 1:
            return 1
        else:
            return func(n)
    return inner

@factorial_decorator
def calculate_factorial(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
    # return n * calculate_factorial(n - 1)

# # Test the decorated function

print(calculate_factorial(5))
# # print(f"Factorial: {result}")




# # def check1(func):
# #     def inner(a,b):
# #         print("in decorator")
# #         if a > 0 and b > 0:
# #             print(func(a,b))
# #     return inner

# # @check1
# # def sum1(a,b):
# #     print("in sum")
# #     return a*b

# # sum1(1,2)

# # # def make_pretty(func):

# # #     def inner():
# # #         print("I got decorated")
# # #         func()
# # #     return inner

# # # @make_pretty
# # # def ordinary():
# #     # print("I am ordinary")

# # # ordinary()



def factorial_decorator(func):
    def inner(n):
        if n < 0:
            return 1
        elif n == 0 or n == 1:
            return 1
        else:
            return func(n)
    return inner

@factorial_decorator
def calculate_factorial(n):
    return n * calculate_factorial(n - 1)

# Test the decorated function

result = calculate_factorial(4)
print(f"Factorial: {result}")


# marks =[56,78,90,100,50]
# get_ave(marks)