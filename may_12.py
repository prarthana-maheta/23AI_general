# # # map(function,iterables)
# # # filter(func,iterables)
# # # reduce(function,iretables,initial)

# # # Write a  Python program that creates a list of dictionaries containing student
# # # information (name, age, grade) 
# # # and uses the filter function to extract students with a grade greater than or equal to 95.


# # students = [
# #     {"name": "Denis Helio", "age": 17, "grade": 97},
# #     {"name": "Hania Mehtap", "age": 16, "grade": 92},
# #     {"name": "Kelan Stasys", "age": 17, "grade": 90},
# #     {"name": "Velvet Mirko", "age": 16, "grade": 94},
# #     {"name": "Delores Aeneas", "age": 17, "grade": 100},
# # ]

# # # x = list(filter(lambda obj : obj.get('grade') >= 95, students))
# # # print(x)

# # # function 
# # # decorators
# # # lambda

# # Dict === key values==items
# # collection modules

# class Example:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

# ex = Example(1,2)

# # # Collection modules

# # # string list tuple set dict 

# # # 1. Counter

# from collections import Counter

# data = Counter('12345678')
# print(data)

# # # # #
# # # # # # Collection modules:
# #
# # 1) Counter
# #
# # class collections.Counter([iterable-or-mapping])


# # A Python program to show different
# # ways to create Counter
# from collections import Counter

# # With sequence of items
# print(Counter(['A', 'B', 'A', 'B', 'C', 'A', 'B',
#                'B', 'A', 'C','B']))

# # with dictionary
# print(Counter({'A': 3, 'B': 5, 'C': 2}))
# #
# # # with keyword arguments
# print(Counter(A=3, B=5, C=2))
# # #
# # #


# # OrderedDict()
# # The Python OrderedDict() is similar to a dictionary
# # object where keys maintain the order of insertion.
# # If we try to insert key again, the previous value will be overwritten for that key.
# d1={}
# d1['A'] = 10
# d1['C'] = 12
# d1['B'] = 11
# d1['D'] = 13
# print(d1)
# import collections

# d1 = collections.OrderedDict()
# # B='B'
# d1['A'] = 10
# d1['C'] = 12
# d1['B'] = 11
# d1['D'] = 13
# # d1[B] = 13
# print(d1)
# for k, v in d1.items():
#     print(k, v)
# # #
# # # #
# # defaultdict()
# # The Python defaultdict() is defined as a dictionary-like object.
# # It is a subclass of the built-in dict class.
# # It provides all methods provided by dictionary but takes the first argument as a default data type.
# # import collections
# # d = collections.OrderedDict(one=1, two=2, three=3)

# # print(d)
# # d1={}


# from collections import defaultdict
# number = defaultdict(list)
# number['one'] = 1
# number['two'] =2
# print(number['three'])
# print(number['four'])
# print(number)
# # coll;ection 

# # a=[1,2,3,54]
# # a.pop()
# # print(a)
# # # # deque()
# # # # The Python deque() is a double-ended queue which allows us
# # # # to add and remove elements from both the ends.
# # # #
# # # # Example
# # # #
# from collections import deque
# list1 = ["x","y","z"]
# deq = deque(list1)
# # # # # # print(deq)
# list1.pop()
# # # # # # print(x)
# deq.popleft()
# deq.pop()
# list1.append('1')
# deq.append('1')
# deq.appendleft('2')
# # # # # # print(x)
# # # # #
# print(list1)
# print(deq)


# # # # Chainmap Objects
# # # # A chainmap class is used to groups multiple
# # # # dictionary together to create a single list.
# # # # The linked dictionary stores in the list and
# # # # it is public and can be accessed by the map attribute. Consider the following example.
# # #
# from collections import ChainMap
# baseline = {'Name': 'Peter', 'Age': '16'}
# adjustments = {'Age': '15', 'Roll_no': '0012'}
# # a={'Age':123}
# # adjustments=[1,2,3]
# # baseline=[4,5,6]
# print(dict(ChainMap(adjustments,baseline)))
# # #
# # #
# # # # NamedTuple()
# # # # # Python code to demonstrate namedtuple()
# # # #
from collections import namedtuple

# # Declaring namedtuple()
Student = namedtuple('Student', ['name','age', 'DOB'])

# # Adding values
S = Student('Nandini','2541997')

# # Access using index
# print("The Student age using index is : ",S)
print(S)
print(S.name)
# # #
# # # # Access using name
# # # print("The Student name using keyname is : ", end="")
# # # print(S.name)
# # # print(S.age)


# # # datetime
# # # time
# # # math
# # # json
# # # regex

# # # pip
# # # pyautogui
# # # random
# # #
# # # try- except
# # # file handling
# # #
# # #
# # # database connection

# # #input
# # input_li=[
# #     {
# #         "User id": 0,
# #         "id": '19',
# #         "User":'dhaval',
# #         'Activities':['sky diving']
# #      },
# # {
# #         "User id": 1,
# #         "id": '20',
# #         "User":'yash',
# #         'Activities':['sky diving']
# #      },
# # {
# #         "User id": 2,
# #         "id": '21',
# #         "User":'dhaval',
# #         'Activities':['driving']
# #      },
# # ]
# # ids=[]
# # activities=[]
# # user_ids=[]
# # users=[]
# # output_list=[]

# # for i in range(len(input_li)):
# #     for j in range(i+1,len(input_li)):


# #         # else:
# #         if input_li[i]['User'] == input_li[j]['User'] :
# #             # activities.extend(
# #             #     (next(iter(input_li[i]['Activities'])),
# #             #      next(iter(input_li[j]['Activities'])),)
# #             #
# #             # )

# #             # output={
# #             #     "User id":input_li[i]['User id'],
# #             #     'id':'_'.join([input_li[i]['id'],input_li[j]['id']]),
# #             #     'User':input_li[i]['User'],
# #             #     'activities': activities
# #             # }
# #             #

# #             print(input_li[i]['Activities'].extend(input_li[j]['Activities']))
# #             # output_list.append(output)
# #             input_li[i]['Activities'] = input_li[i]['Activities'].extend(input_li[j]['Activities']),
# #             input_li[i]['User'] = input_li[i]['User']
# #             input_li[i]['id'] = '_'.join([input_li[i]['id'],input_li[j]['id']])
# #             input_li.remove(input_li[j])
# #         # if input_li[i]['User'] != input_li[j]['User']:
# #         # else:
# #         # elif input_li[i] not in output_list and input_li[j] not in output_list :
# #         #         output_list.append(input_li[i])
# #         # elif input_li[j] not in output_list :

# # print(input_li)
# # print(output_list)

# # # ids=[]
# # # activities=[]
# # # user_ids=[]
# # # users=[]
# # # output_list=[]
# # # for element in input_li:
# # #     if element['User'] not in users:
# # #         users.append(element['User'])
# # #
# # #     if element['User'] in users:
# # #         ids.append(element['id'])
# # #         activities.append(next(iter(element['Activities'])))
# # #         user_ids.append(element['User id'])
# # #         print(ids,activities,user_ids)
# # #         output={
# # #         # 'User id' : user_ids[0],
# # #         'User' : element['User'],
# # #         'Activities' : activities,
# # #         # 'id': '_'.join(ids)
# # #             }
# # #         print(output)
# # #         output_list.append(output_list)
# # # print(output_list)
# # #output
# # # [
# # # {
# # #         "User id": 0,
# # #         "id": '19_21',
# # #         "User":'dhaval',
# # #         'Activities':['sky diving','driving']
# # #      },
# # # {
# # #         "User id": 1,
# # #         "id": '20',
# # #         "User":'yash',
# # #         'Activities':['sky diving']
# # #      },
# # # ]



