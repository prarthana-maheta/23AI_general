from _ast import arguments


# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.
# def abc():
#     print("Hello from a function")
# abc()

# def my_function(a):
#     print(a + " abc")
#
# my_function("123")
# my_function("234")
# my_function("356")

#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# A parameter is the variable listed inside the parentheses in the function definition.
#
# An argument is the value that is sent to the function when it is called

# def my_function(fname, lname):
#   return f"{fname} {lname}"
#
# result=my_function("Emil", "Refsnes")
# print(result)


# def my_function(param1, param2=2):
#     return param1 + param2
#
# print(my_function(1,5))

# def my_function(param2, param1):
#     return param1 - param2
# print(my_function(param1=2,param2=6))
#
# def add_of_min_max(one,two,four,five,three=7):
#     list1=[one,two,four,five,three]
#     # list1.extend([one,two,four,five,three])
#     return min(list1)+max(list1)
#
# print(add_of_min_max(one=89,two=56,four=6,five=45))

# take 5 user arguments

# ********Arbitrary Arguments, *args
# arguments that will be passed into your function, add a * before the parameter name in the function definition.
# def my_function(*kids):
#     print(kids)
#     for i in kids:
#         print("The youngest child is " + i[0])
# #
# my_function("Emil", "Tobias", "Linus","cgvdgc","jxgscv")



# Keyword Arguments
# You can also send arguments with the key = value syntax.
# def my_function( child2, child1,child3):
#   print("The youngest child is " ,child3)
#
# my_function(child1="Emil", child2="Tobias", child3="Linus")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments
# that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.


# {
#     "fname":"1",
#     "lname":"2"
# }
def my_function(**kid):
  print(kid["fname"] + kid["lname"])

my_function(fname = int(input("enter one number")), lname = int(input("enter one number")))



# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)
