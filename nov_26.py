# l1=[1,2,3]
# print(l1)


# if name == 'pkm':
#     print("3")

# if a==3:
#     print("5")
#     if a==5:
#         print("3")
#     else:
#         print("else")
# else:
#     print("if")
#     if a==1:
#         print("1")
#     else:
#         print("child")
# a=5
# if a==3:
#     print("5")
# elif 1==0:
#     print("1")
# elif 6==5:
#         print("3")
# else:
#     print("2")


#     del l1[1]
    # else:
    #     print("hello")
#
#



# print(l1)

# take input as your name, check whether your name entered is correct or not

# find greater number from two numbers

# find maxnimum number between three elements

# to check whether a person is eligible for voting
#
# check whether person is senior citizen
#
# write a program to check whether a number is positive or negative
#
# write  program to check whether a number is odd or even


# n1 = int(input("Enter number 1 : "))
# n2 = int(input("Enter number 2 : "))
# n3 = int(input("enter number 3: "))
#
# list_items=[n1,n2,n3]
# print(max(list_items))


# if n1 > n2 and n1> n3:
#     print(n1,"is greater")
# elif n2 > n3:
#     print(n2,"is greater")
# else:
#     print("n3 ")

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is bigger..")
# elif num2 > num3 and num2 > num1:
#     print(f"{num2} is bigger..")
# else:
#     print(f"{num3} is bigger..")


# Write a Python program that takes input as interger
# For multiples of three print "Fizz" instead of the number and
# for multiples of five print "Buzz".
# For numbers that are multiples of three and five, print "FizzBuzz".



# looping through string
# a="banana"
# for x in a:
#     print(x)
#
# # looping through list
# fruits = ["apple", "1", "cherry"]
# for x in fruits:
#     for y in x:
#         if "a" in y:
#             print("yes")
#         print(y)
#     print(x)




# With the break statement we can stop the
# loop before it has looped through all the items:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# Exit the loop when x is "banana", but
# this time the break comes before the print:
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     for y in x:
#       if x == "banana":
#         print(y)
#         break
#         print(y)
#     print(x)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     for y in x:
#       if x == "banana":
#         continue
#         print(y)
#         print(x)
#     print(x)


# With the continue statement we can stop
# the current iteration of the loop, and continue
# with the next:
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits[::-1]:
#     for y in x[::-1]:
#         print(y)
#     if x == "banana":
#         print(x)
#
fruits = ["apple", "banana", "cherry"]
# print(list(reversed(fruits)))
# for x in reversed(fruits):
#   if x == "banana":
#     print(x)

# print(list(reversed(fruits)))
# print(fruits)
# # print(fruits.reverse())
# fruits.reverse()
# print(fruits)

# for loops cannot be empty, but if you for some
# reason have a for loop with no content, put in
# the pass statement to avoid getting an error.
#
# for x in [0, 1, 2]:
#
#     print(x)

# having an empty for loop like this,
# would raise an error without the pass statement

# pop()


# The range()
# function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(-1,5,-1):
  print(x)

# for x in range(-1,1,3):
#   print(x)


#start,stop,increment
# for x in range(2, 30, 3):
#   print(x)

# Example 1: Print the first 10 natural numbers using for loop.
# Example 2: Python program to print all the even numbers within the given range.
# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
# Example 5: Python program to print a multiplication table of a given number


# Example 6: Python program to count the total number of digits in a number. example:-1ab128hdv
# Example 7: Python program that accepts a word from the user and reverses it.
# Example 8: Python program to count the number of even and odd numbers from a series of numbers. 133456789
# Example 9: Python program to find the factorial of a given number.


list1=[1,2,3,5,6]
even_c=0
odd_c=0
for i in list1:
  if i %2 ==0:
    even_c+=1
  else:
    odd_c+=1

print(even_c,odd_c)
# for i in list1:
#   # print(i)
#   if i == 5:
#     break
#   print(i+1)
# i=2
# while i==2:
#   i+=1
#   print(i**3)


# str1 ='abc12abc21'
# counter = 0
# for i in str1:
#
#   if i.isdigit():
#     counter+=1
# print(counter)


# str1="abc"
# list2=list(str1)
# # abc=list(reversed(str1))
# print("".join(reversed(str1)))
# print(list2)

# list1=['a',"b","c"]
# print("".join(reversed(list1)))
# list1.reverse()
# print("".join(list1))







#######################1############
# # between 0 to 10
# # there are 11 numbers
# # therefore, we set the value
# # of n to 11
# n = 11
#
# # since for loop starts with
# # the zero indexes we need to skip it and
# # start the loop from the first index
# for i in range(1, n):
#     print(i)



#######################2########################
# # if the given range is 10
# given_range = 10
#
# for i in range(given_range):
#
#     # if number is divisble by 2
#     # then it's even
#     if i % 2 == 0:
#         # if above condition is true
#         # print the number
#         print(i)


################3##############

# # if the given number is 10
# given_number = 10
#
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
#
# # since we want to include the number 10 in the sum
# # increment given number by 1 in the for loop
# for i in range(1, given_number + 1):
#     sum += i
#
# # print the total sum at the end
# print(sum)


###############4##############

# # if the given range is 10# Example 7: Python program that accepts a word from the user and reverses it.
# Example 8: Python program to count the number of even and odd numbers from a series of numbers.
# Example 9: Python program to find the factorial of a given number.
# given_range = 10
#
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
#
# for i in range(given_range):
#
#     # if i is odd, add it
#     # to the sum variable
#     if i % 2 != 0:
#         sum += i
#
# # print the total sum at the end
# print(sum)


################5#####################


# # if the given range is 10
# given_number = input()
#
# for i in range(11):
#     print(f"{given_number}x{i}=",given_number * i)


####################6#####################

#
# # if the given number is 129475
# given_number = 12345
# # for i in given_number:
# #     print(i)
# # # since we cannot iterate over an integer
# # # in python, we need to convert the
# # # integer into string first using the
# # # str() function
# given_number = str(given_number)
# #
# # # declare a variable to store
# # # the count of digits in the
# # # given number with value 0
# count = 0
# #
# for i in given_number:
#     if i.isdigit():
#         count += 1
# #
# # # print the total count at the end
# print(count)




# gn=list(given_number)
# print(len(gn))



#######################7#################

# # input string from user
# given_string = input()
# print(given_string[::-1])
#
# # an empty string variable to store
# # the given string in reverse
# reverse_string = ""
#
# # iterate through the given string
# # and append each element of the given string
# # to the reverse_string variable
# for i in given_string:
#     reverse_string = i + reverse_string
#
# # print the reverse_string variable
# print(reverse_string)




#################10##################

# given list of numbers
# num_list = list(input())
# print(type(num_list))
# print(num_list)
# iterate through the list elemets
# using for loop
# e=0
# o=0
# for i in num_list:
#
#     # if divided by 2, all even
#     # number leave a remainder of 0
#     if i % 2 == 0:
#         e+=1
#         print(i, "is an even number.")
#
#     # if remainder is not zero
#     # then it's an odd number
#     else:
#         o+=1
#         print(i, "is an odd number.")
#
# print(o,e)


######################9#################


# given number
given_number = 5

# since 1 is a factor
# of all number
# # set the factorial to 1
# factorial = 1
#
# # iterate till the given number
# for i in range(1, given_number + 1):
#     factorial = factorial * i
#     print(factorial)
#
# print("The factorial of ", given_number, " is ", factorial)