# Those modules which came directly with python installation - inbuilt modules
# help('modules')

# math
# random
# datetime
# urllib3.request

# csv
# json

import math

# print(dir(math))

# print(help(math))

# print(dir(math))

# print(math.pow(4,3))
# print(math.e)
# print(math.pi)

# print(math.sqrt(54))
# print(math.floor(4.76))

# print(math.gcd(12,14))

# Random Module

import random

# print(dir(random))

# print(random.random()) # will return the random floating value between 0 and 1..

# print(random.randint(12,65))

# print(random.randint(100000,999999))

# print(random.randrange(100000,999999))


# print(random.randrange(3,46,4)) # [3,7,11,15,19,23,27,31,35,39,43]


# a=['ramesh','suresh','mahesh','subash','venkatesh','rajesh','kumar']

# print(random.choice(a))
# print(random.choices(a,k=2))

# datetime module..

# import datetime
from datetime import datetime

# print(dir(datetime))

print(datetime.now())

# print(datetime.now().date())

# print(datetime.now().time())

# print(datetime.now().date().weekday())

# print(datetime.now().time().second)

# print(datetime.utcnow())

from datetime import timedelta

# after_25 = datetime.now() + timedelta(days=25)

# print(after_25)

# after_10min = datetime.now() + timedelta(minutes=10)

# print(after_10min)

# print(type(after_10min))

# now_date = datetime.now() + timedelta(hours=5)

# data = now_date.strftime('%Y')

# data = now_date.strftime("%d/%m/%Y %I:%M %p")
# print(data)
# print(type(data))


# strptime()..

# today_date = "24 Feb 2023 09:50"

# print(today_date)
# print(type(today_date))

# con_date = datetime.strptime(today_date,'%d %b %Y %H:%M')

# print(con_date)

# print(type(con_date))


# import urllib.request

# data = urllib.request.urlopen("https://www.programiz.com/python-programming/datetime/strptime")

# print(data.read())