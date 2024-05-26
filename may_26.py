# requests

# GET - read data 
# POST - store 
# PUT -update 
# PATCH - partial update
# DELETE -delete stored data


# import requests

# response = requests.get('https://images.pexels.com/photos/60597/dahlia-red-blossom-bloom-60597.jpeg')

# # print(response.__dict__)

# with open('content.jpeg','wb') as f:
#     f.write(response.content)


# json
# import json
# str1='{"123":"asd"}'

# # print(type(str1))
# # a=json.loads(str1)
# # print(a)
# # print(type(a))

# str2={"123":"asd"}
# print(type(str2))
# a=json.dumps(str2)
# print(a)
# print(type(a))

# datetime

from datetime import datetime 

# print(datetime.now())

# d=datetime.now()
# print(d)

# int_sr="25 May, 2024"

# print(datetime.strptime(int_sr,"%d %B, %Y"))


# d=datetime.now()
# print(d)
# print(d.strftime('%d/%m/%y'))

# from datetime import datetime, date

# # using date()
# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)

# t3 = t2 - t1

# print("t3 =", t3)

# # using datetime()
# t4 = datetime(year = 2019, month = 6, day = 10, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t5 - t4
# print("t6 =", t6)

# print("Type of t3 =", type(t3)) 
# print("Type of t6 =", type(t6))  


# from datetime import timedelta

# t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

# t3 = t1 - t2

# print("t3 =", t3)


from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))