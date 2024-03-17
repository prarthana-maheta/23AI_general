

# # String 
# # list
# # tuple
# set

# dictionary


# # function Base
# # OOPs

# # brand="brand"
# thisdict = {"&": None,
#             "model": [None, "abc"],
#             "year": 1964,
#             "brand":"tata"
#             }

# # Dictionaries are used to store data values in key:value pairs.
 
# # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# two='two'
# thisdict ={
#     1:"one",
#     '2':'two'
# }
# print(thisdict)
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    
}
# my=[1,2,3]
# # # print(thisdict)
# # # functions:
# print(type(thisdict))
# print(len(thisdict))
# print(tuple(thisdict))
# print(dict(my))


# # # Accessing dict:

# thisdict = {
#     "brand": "Ford",
#     "mode": "Mustang",
#     "year": 1964
# }
# print(thisdict["brand"])

# print(thisdict.get("brande","mercedes"))

# print(thisdict.keys()) #--->[keys]
# print(thisdict.values())

# # print(thisdict.keys())
# # # #

# for keys in thisdict.keys():
#     if keys == 'model':
#         print(thisdict['model'])
# print(thisdict.values().append("1"))

# x=thisdict.items()
# print(x)
# for k,v in thisdict.items():
#     print(k,v) 
# # # # print(x[0])
# # # for i,j in x:
# # #     print(i)
# counter=0
# {
#     'one':100,
#     'two':200,
#     'three':300,
#     'five':500,
# }

# for k,v in thisdict.items():
#     if k =='one':
#         counter += v*1
#     if k =='two':
#         counter += v*2

# thisdict={
#     1:1,
#     2:2,
#     3:3,
#     4:4,
#     5:5
# }
# [1,4,9,16,25]        


# list1=[]
# for k,v in thisdict.items():
#     list1.append(v*k)
# # [1,4,9,16,25]
# print(list1)

# # # add data to dict:
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     # "year": "blue",
# }
# #
# # x = car.items()
# print(car) #before the change
# car["year"] = None
# print(car)  # after the change

# # # change values of dict:
# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict["year"] = 2018

# # # update dict:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
#   "year": 1964
}
thisdict.update({"year": 2024},{'abc':34},price=300000,ad=123)
print(thisdict)


create one empty dictionary

add   name key  and  Value 
add roll no key and Value
add subject key and list of subjects as value ['python','java']
add batch as key and its Value


add one more subject to the subject key 'c++' 
update the batch Key


# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict.update({"year": 2020})
