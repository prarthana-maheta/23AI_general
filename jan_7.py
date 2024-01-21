#
#
# # list vs tuple
#
# # []
# # ()
#
# # thistuple = ("apple", "banana", "cherry",1,[1,2,3])
# # # thistuple[4] = '123'
# # # thistuple[4].append(5)
# # # # thislist=[1,2,3]
# # print(thistuple)
#
#
# # Ordered
# # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# #
# # Unchangeable/Immutable
# # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# #
# # Allow Duplicates
#
#
# # print(type(thistuple))
# # print(len(thistuple))
# #
# # thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # tuple(thistuple)
# # print(thistuple[5:1:-1])
#
# # check if present
# # thistuple = ("apple", "cherry", "apple")
# # if "apple" in thistuple:
# #     print("Yes, 'apple' is in the fruits tuple")
# # if "cherry" in thistuple:
# #     print("yes, 'cherry' in ")
#
#
#
#
#
# # change tuple value update tuple
# #
# x = ('1',"apple", "banana", "cherry",'2','3')
# # x[1] = 'melon'
# print(x)
# y = list(x)
# print(y)
#
# y[0] = "kiwi"
# #
# print(y)
# x = tuple(y)
# #
# print(x)
#
#
# # add items to tuple
# # thistuple = ("apple", "banana", "cherry")
# # y = list(thistuple)
# # y.append("orange")
# # thistuple = tuple(y)
#
#
# # thistuple = ("apple", "banana", "cherry")
# # y = list(thistuple)
# # y.remove("apple")
# # thistuple = tuple(y)
#
#
#
# # # unpack tuple
# fruits = ("apple", "banana", "cherry",'1')
#
# green, yellow, red,one = fruits
# print(green, yellow, red,one)
#
#
# # pack=green,yellow,red
# # print(pack)
# # #
# # print(green)
#
# # print(yellow)
# # print(red)
#
#
# # fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# # yellow,*red = fruits
#
# # print(green)
# # print(yellow)
# # print(red)
#
# # tuple method
# # count,index
#
#
#
# #loop through tuple
# # thistuple = ("apple", "banana", "cherry")
# # for x in thistuple:
# #     for i in x:
# #         print(i)
# #   print(x)
#
# # thistuple = ("apple", "banana", "cherry")
# # for i in range(1,len(thistuple),2):
# #   print(thistuple[i])
#
#
# # while loop in tuple
#
# # thistuple = ("apple", "banana", "cherry","abc")
# # i = 0
# # while i < len(thistuple):
# #     print(thistuple[i])
# #     i = i + 1
#
#
# # join two tuple
# # tuple1 = ("a", "b" , "c")
# # tuple2 = (1, 2, 3)
# # #
# # tuple3 = tuple1 + tuple2
# # print(tuple3)
#
# # l1=["hello"]
# # print(l1+l1)
#
# # # Multiply two tuple
# # fruits = ("apple", "banana", "cherry")
# # mytuple = fruits + fruits
#
# # print(mytuple)
#
#
#
#
#
# # thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#
# # x = thistuple.count(5)
#
# # print(x)
#
# # thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#
# # x = thistuple.index(8)
#
# # print(x)
#
#
# Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
#
#
# Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648
#
#
# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))
