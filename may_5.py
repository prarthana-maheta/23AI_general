# map 
# lambda 
# filter 
# reduce 


# map(func1,iterables)


# # Filter
# # While map() passes each element in the iterable through
# # a function and returns the result of all elements having passed through the function,
# # filter(), first of all, requires the function to return boolean values (true or false)
# # and then passes each element in the iterable through the function,
# # "filtering" away those that are false. It has the following syntax:
# #
# filter(func, iterable)
# #
# # The following points are to be noted regarding filter():
# #
# # Unlike map(), only one iterable is required.
# # The func argument is required to return a boolean type.
# # If it doesn('t, filter simply returns the iterable passed to it. Also, as only one iterable is required, '
# #             'it')s implicit that func must only take one argument.
# # filter passes each element in the iterable through func
# # and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".
# #
# #
# # # Python 3
# dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

# palindromes = list(filter(lambda word: word == word[::-1], dromes))

# print(palindromes)



# x = list(filter(lambda even: even%2==1,range(1,101)))
# print(x)



# # Reduce
# # reduce applies a function of two arguments cumulatively
# # to the elements of an iterable, optionally starting with an initial argument. It has the following syntax:
# #
# reduce(func, iterable, initial)
# #
# # Where func is the function on which each element
# # in the iterable gets cumulatively applied to,
# # and initial is the optional value that gets placed before the elements of the iterable in the calculation,
# # and serves as a default when the iterable is empty. The following should be noted about reduce():
# # 1. func requires two arguments, the first of which is the first element in iterable
# # (if initial is not supplied) and the second element in iterable. If initial is supplied,
# # then it becomes the first argument to func and the first element in iterable becomes the second element.
# # 2. reduce "reduces" (I know, forgive me) iterable into a single value.

# # Python 3
# from functools import reduce
# # #
# numb= int(input("enter num"))

# def custom_sum(first,num):
    
#     return first*num

# result = reduce(custom_sum, range(1,numb+1),5)
# print(result)
# print(sum(numbers))


















from functools import reduce

# reduce(func1,iterable,initial)

# # Use map to print the square of each numbers rounded
# # to three decimal places
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# # Use filter to print only the names that are less than
# # or equal to seven letters
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# # Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# # Fix all three respectively.
# map_result = list(map(lambda x: x, my_floats))
# # filter_result = list(filter(lambda name: name, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers,10)

# # print(map_result)
# # print(filter_result)
# print(reduce_result)





# Write a Python class Inventory with attributes 
# dict key: day_out_list
#methods like add_item, update_item, and check_item_details,purchase
# Use a dictionary to store the item details, 
# where the key is the item_id and 
# the value is a dictionary containing the item_name, stock_count, and price.

items={
    '123':{
        "item_name":"Books",
        "stock_count":10,
        "price":200
    }
}