vegetables = ["carrot", 123, "potato", "spinach", "cucumber", "beetroot", "onion", "Lemon"]
# print(vegetables)
# print(min(vegetables))
# print(max(vegetables))
# numbers=[33, 10, -125, 44, 33, 4791234, -5592, 33]

# task:
# 1) sort it in desc
# 2)find min, max
# 3) print(patato,spinach,cucumber)
# ans:
# veg=vegetables
# print(veg)
# veg[1]=str(veg[1])
# print(sorted(veg,reverse=True))
#
# print(min(veg))
# print(max(veg))
vegetables = ["carrot", 123, "potato", "spinach", "cucumber", "beetroot", "onion", "Lemon"]
# print(len(vegetables))
# vegetables[9]=3333
# print(vegetables)
#
# vegetables.append(["12345","34566"])
# # # numbers.append("12345")
# vegetables.insert(3,"fhvhffv")
# vegetables.extend([34,56,78],{"hbhdhcv"})

# print(vegetables)

# # Mutable
# # numbers[3] = 119.8
# # print(numbers)
#
# # list methods
# numbers.append(2000)
#
# numbers.append(3000)
# # print(numbers)
# # numbers.append(3000)
# # numbers.append(3000)
# # print(numbers)
# # numbers.append(3000)
# # print(numbers)
# #
# # numbers=[1,2,3]
# # print(numbers)
# # numbers.clear()
# print(numbers)
# # numbers.append(1)
#
# # del numbers[2]
# print(numbers)
#
# print(numbers.count(10))
#
# s1="aaaaaa"
# print(s1.count('s',2,4))
# print(numbers.count('s'))
#
#
#
#
#
li=[1,2,3,4,5,6,7,8,9,0]
# # output:

# [1,3,5,7,9]
# [1,0]
# [1,2,3,4,5,6,7,8,9,0,"i",55]
# [1,2,"in","out","upper",3,4,5,6,7,8,9,0]
# ["first",2,3,4,"five",6,7,"eight",8,9,0]

# li=[1,2,3,4,5,6,7,8,9,0]
# print(li.count(1))

l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# l2=l1
# l1[0] = "123"
# l2[0]='345'
# print(l2)
# print(l1)
# print(l2)

# l2 = l1.copy()
# l1[0] = "123"
# l2[0]='345'
# print(l2)
# print(l1)
# print(l2)


l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]

# ans=l1.pop(-1)
# print(ans)
# print(l1)

# l1.remove(33)
# print(l1)

# l1.clear()
# print(l1)
# l1.append(1)
# print(l1)

# del l1
# print(l1)

# # # del l1
# # # print("Before:")
# # # # print("l1 =", l1)
# # # print("l2 =", l2)
# # # l3 = l1
# # # print("l3 =", l3)
# #
# # # l1.append(5000)
# #
# # # print("After:")
# # # print("l1 =", l1)
# # # print("l2 =", l2)
# # # print("l3 =", l3)
# #
# # # del l1
# # # print(l1)
# # l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# # l2=[100,500,"abc"]
# # l1.extend(l2)
# # print(l1)
# # l1.insert(4, "5")
# # print(l1)
# # # l2 = [100, 200, [300,123]]
# # # l3=[1]
# # # l1.append(l2)
# # #
# # # l2.extend(l3)# print(len(l1))
# # # l1.extend(l2)
# # # print(l1)
# #
# # # l3 = "Python"
# # # l1.extend(l3)
# # # print(len(l1))
# # # print(l1)
# #
# l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# print(l1.index(44))

# print(l1.find(44))
# # # print(l1.index(33, 4))
# # print(l1.index(33, 4, 6))
# #
# # #
# # # print(l1)
# # li=["123",1,2,3]
# # # print(l1.pop())
# # print(li.pop(0))
# # # # print(l1.pop(500))
# # print(li)
# #
# # li.remove(1)
# # # # print(l1.remove(-50592.44))
# # # print(li)
l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]
# l1.append(['1'])
# l1.extend(['1'])


l2=l1.reverse()
print(l1)
# print(l2)#----> new list
print(list(reversed(l1)))
#----->object
# #
# #
# # # print("l1 =", l1)
# # # print(list(reversed(l1)))
# # #
# # sorted(l1,reverse=True)
# # l1.sort()
# # l1.sort(reverse=True)
# # print("l1 =", l1)
#
# # l1.reverse()
# # print("l1 =", l1)
#
# # list1=[100,45,23,67,123,67,89]
# #
# # output:
# # 1) minimun
# # 2)maximum
# # 3)asecding
# # 4)desending
#
# # list1=[1,2,3,4]
# # 5)list2=["!","123",""] add this list to list1
# # 6) delete list1 and print list1
# #
# #
# # delete list
# # print(list2)
#
# # list2=[1,2,3]
# # print(sum(list2))
# #
# # list1[2,56,34,67,89]
# #
# # total of list1
# # use reversed on list1
# # [2,34,89]
#


#
#
# # Next Class: Operators in Python, decision making, loops, remaining collections
#

Task:

l1 = [33, 0, -125, 44.6, 33, 4791234, -5592.44, 33, 1000]

1)delete the 1000 value
2) delete -125 and add it at the end of the list
3) reverse the list and extend that reversed list to l1

