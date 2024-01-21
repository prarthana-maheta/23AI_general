# looping through string
# a="banana"
# for x in a:
#     print(x)
#
# # looping through list
# fruits = ["apple", "1", "cherry"]
# counter=0
# for x in fruits:
#     for y in x:
#         if y == 'r':
#             continue
#         print(y)
#     # counter += 1
#     # fruits.append(counter)
#     # if counter == 10:
#     #     break
#     print(x)
#
#


# With the break statement we can stop the
# loop before it has looped through all the items:
#
# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #   print(x)
# #   if x == "banana":
# #     break
#
#
# # Exit the loop when x is "banana", but
# # this time the break comes before the print:
# #
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     for y in x:
#       if x == "banana":
#         print(y)
#         break
#         print(y)
#     print(x)

#
# # With the continue statement we can stop
# # the current iteration of the loop, and continue
# # with the next:
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits[::-1]:
#     for y in x:
#         print(y)
#   # if x == "banana":
#     print(x)
# #
fruits = ["apple", "banana", "cherry"]
# for x in reversed(fruits):
#   # if x == "banana":
#     print(x)
#
# # print(list(reversed(fruits)))
# print(fruits)
# # print(fruits.reverse())
# fruits.reverse()
# print(fruits)
# # for loops cannot be empty, but if you for some
# # reason have a for loop with no content, put in
# # the pass statement to avoid getting an error.
# #
# # for x in [0, 1, 2]:
# #
# #     print(x)
#
# # having an empty for loop like this,
# # would raise an error without the pass statement
#
# # pop()
#
#
# # The range()
# # function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# # for x in range():
# #   print(x)
#


# abc=[1,2,3,4,5,6,7,8,9]
# for x in range(len(abc)):
#     if x == 7:
#         abc[x] = 10
#     print(x)
# print(abc)


#
# #start,stop,increment
# # for x in range(2, 30, 3):
# #   print(x)

# 1) 1-100 find even numbers and get the sum of them
# 2) reverse a list
# 3) remove duplicate from a list list1=[1,2,'1',2,3,4,4,5,4]


# list1=[]
# sum=0
# for i in range(0,101,2):
#     if i % 2 == 0:
#     #     # list1.append(i)
#         sum += i
# # print(sum(list1))
# print(sum)

# list1=[1,2,3,4,5,6,7,8,9]
#
# list1.reverse()
# print(list1)


# list1=[1,2,'1',2,3,4,4,5,4]
#
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# print(list(set(list1)))



# Example 1: Print the first 10 natural numbers using for loop.
# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
# Example 5: Python program to print a multiplication table of a given number
# Example 6: Python program to count the total number of digits in a str.


# Example 7: Python program that accepts a word from the user and reverses it.
# Example 8: Python program to count the number of even and odd numbers from a series of numbers.
# Example 9: Python program to find the factorial of a given number.
