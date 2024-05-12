# lambda---ano  dunc , small code snippet 


# def func(b):
    # return b*b 

    # code 
# lambda arguments: expressions

# x = lambda arg1,arg2: {arg1:arg2}
# print(x(1,"hello"))

# def finding(num):
#     if num %2==0:
#         print("yes")
#     else:
#         print('NO')
# list1=[1,2,3,4,5,6,7,8,9]

# x= lambda num: print("yes") if num%2 == 0 else print("No")

# x= lambda list1: [i for i in list1 if i%2==0 ] 
# x= lambda list1: [i if i%2==0  else 0 for i in list1 ] 
# print(x(list1))


# map --mapping
def function1(n):
    return n*n
# for i in num:
#     function(i)

# map(function,iterable)

# print(list(map(lambda x,z: {x:z}, [1,2,3,4,5],[5,6,7,8,9,9],[4,5])))
# print(list(map(lambda x: [i for i in x if i.isalpha()], ['abc','567'])))

print(dict(map(lambda x,y: (f"{x}_{y}", f"{y}_{x}"), ["1","2","3","4","5"], ["a","b","c","d","e"])))