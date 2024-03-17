# Write a Python program to filter a dictionary based on values.
# # Original Dictionary:
# a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165,
#  'Pierre Cox': 190}
# # Marks greater than 170:
# expectd:{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

# removing from dict
# dict1={
#     "a":"apple",
#     "b":"ball",
#     "c":"cat"
# }
# dict2 = dict1.copy()
# dict3=dict1
# dict1.pop("a")
# print(dict1)
# print(dict2)
# print(dict3)

# ans=dict1.pop("a")
# print(ans)
# print(dict1)

# ans1=dict1.popitem()
# print(dict1,ans1)
# dict1.clear()
# print(dict1)
# del dict1["a"]
# print(dict1)
# # # remove items:
# # #
# # # # 1) pop()
# # # thisdict = {
# # #   "0": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict.pop("model")
# # # print(thisdict)
# # #
# # # # 2)popitem()
# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict.popitem()
# # # print(thisdict)

# # # 3)del
# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964

# # # }
# # # del thisdict['band']
# # # print(thisdict)

# # # 4)clear()
# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict.clear()
# # # print(thisdict)
# # # thisdict['a']=1
# # # print(thisdict)

# 5)copy()
c=[2,3]
a=[1,2]
b=c.copy()
del a
print(b)


# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # mydict = thisdict.copy()
# # # del thisdict
# # # # print(thisdict)
# # # print(mydict)

# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # mydict = dict(thisdict)
# # # print(mydict)

# # # 6) setdefault()
# # # car = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # print(car.setdefault("color", "white"))
# # # print(car)
# # # print(car.setdefault("color", "black"))
# # # car.update({"color": "red"})
# # # car.update({"color": "pink"})
# # # print(car)
# # # print(x)

# # # 7) fromkeys()
# # x = ('key1', 'key2', 'key3')
# # y=(1,2)
# # # thisdict = dict.fromkeys(x,y)
# # thisdict=list(zip(x,y))
# # print(thisdict)

# # # nested dict:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
   "child1":None,
  "child2" : child2,
  "child3" : child3
}
# # # #
print(myfamily)
# # #
print(myfamily["child2"]["name"])
print(myfamily.get("child2").get("name"))

# # child1 = {
# #     "name": "Emil",
# #     "year": 2004
# # }
# # child2 = {
# #     "name": "Tobias",
# #     "year": 2007
# # }
# # child3 = {
# #     "name": "Linus",
# #     "year": 2011
# # }
# # myfamily = {
# #     "child1": "abc",
# #     "child2": "abc",
# #     "child3": "abc"
# # }

# # # for key,value in myfamily.items():
# # #     print(key)
# # #     # myfamily[key]="abc"
# # #     # print(myfamily)
# # #     # print(value)
# # #
# # #     if "child1" == key or "child2" in key :
# # #         print("found")
# # #
# # # if "child1" in myfamily.keys():
# # #     print("yes")

# # # l1=['a', 'b', 'c', 'd', 'e', 'f']
# # # l2=[1, 2, 3, 4, 5]
# # # print(dict(zip(l1,l2)))

# # myfamily = {
# #     "child1": "abc",
# #     "child2":
# #         {"abc":1},
# #     "child3": "abc"
# # }
# # # myfa=myfamily
# # # myfam=myfamily.copy()
# # # myfamily['change']=1
# # # print(myfa)
# # # print(myfam)
# # for i,j in myfamily.items():
# #     if isinstance(j,dict):
# #         print("yes")

# student--main dict
# "name":"student name"
# "roll no": int
# "department":{
#     # "name":string,
#     "sub-dept":""
# }

# student={
# }

# student["name"]="a"
# student["roll no"]=1
# student["department"]={}
# student.update({"department":{"name"}})

# l1=[1,2,3]
# l2=[3,4,5,4]
# # l3=[6,7,8]
# print(dict(zip(l1,l2)))

# dict1={
#     "one":1,
#     "two":2,
#     "three":3
# }

# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output:
# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

input_str=input()
output_dict={}
for i in input_str:
    # if i not in output_dict:
        output_dict[i] = output_dict.get(i,0) + 1