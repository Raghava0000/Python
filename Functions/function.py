# # functions : Set of line of code which performs a specific task..


# # Main feature of function is code reusuability..


# # a=5
# # b=6


# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)


# # print("-------------------------------------------------------------")
# # a=10
# # b=11

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)

# # Function syntax:

# """
# def function-name():
#     statements
# """

# # a=5
# # b=6

# # def arthimetic():
# #     print(a+b)
# #     print(a-b)
# #     print(a*b)
# #     print(a/b)


# # # Without calling the function nothing will get executed inside the function..

# # # calling funtion:

# # arthimetic()

# # a=10
# # b=11
# # print("--------------------------------------------------------------------")
# # arthimetic()

# # print(a)
# # print(b)

# # Passing arguments to the function..

# # 1) Positional arguments
# # 2) Default Arguments
# # 3) Keyword Arguments
# # 4) Arbitrary Positional Arguments
# # 5) Arbitrary Keyword Arguments

# # def arthimetic(a,b):
# #     print(a+b)
# #     print(a-b)
# #     print(a*b)
# #     print(a/b)

# # print('first-1')
# # arthimetic(5,6)
# # print('second-2')
# # arthimetic(int(input("Enter a value:")),int(input("Enter b value:")))

# # print(a)
# # print(b)

# # Positional arguments : Assigning the values to the arguments based on the position..

# # def employee_info(name,emp_id,emp_loc):
# #     print(f"Hello {name},your employee id is {emp_id} and your work location is {emp_loc}")

# # employee_info('ramesh','89383','Financial district')

# # employee_info('ramesh','89383')

# # employee_info('89383','Financial district','ramesh')


# # Default arguments: Passing the default value to an argument at the declaration itself.
#     # if value to that argument is passed at function call, that valuw will be considered. If no value is passed default value will be taken into consideration..


# # def employee_info(name,emp_id,emp_loc='Gachibowli'):
# #     print(f"Hello {name},your employee id is {emp_id} and your work location is {emp_loc}")


# # employee_info('suresh','738728','Cyber Gateway')

# # employee_info('suresh','738728')


# # def employee_info(name,emp_id="New",emp_loc="Gachibowli"): # We cannot declare positional arguments after declaring default argument(invalid syntax)..
# #     print(f"Hello {name},your employee id is {emp_id} and your work location is {emp_loc}")


# # employee_info('suresh','738728','Cyber Gateway')

# # employee_info('suresh','738728')


# # Keyword arguments:

# # def employee_info(name,emp_id,emp_loc): 
# #     print(f"Hello {name},your employee id is {emp_id} and your work location is {emp_loc}")


# # print(employee_info(emp_loc="Hitech city",name="venkatesh",emp_id='8389983'))


# # employee_info('mahesh',emp_id='8939833',emp_loc='Jubilee hills')

# # employee_info('subash',emp_id=9303093,'Bnajara hills') # will give the error, becuase once a keyword argument is declared afterthat everythhing should be keyword arguments only..


# # employee_info('manik',emp_id='7398383',emp_loc='kukatpally',name="basha") # will pass multiple values for name, so it will through the error.


# # Arbitrary Positional arguments.. : Its for taking multiple no.of positional arguments

# # * -- for declaring the arbitrary positional arguments..

# # def cred_trans(*trans):
# #     print(trans)
# #     # print(type(trans))
# #     total_amt = 0
# #     # for ele in trans:
# #     #     if type(ele) == int:
# #     #         total_amt = total_amt+ele
# #     #     else:
# #     #         name = ele
# #     name = trans[0]
# #     for ele in trans[1:]:
# #         total_amt+= ele
# #     # print(total_amt)
# #     print(f'Hi {name},You have performed {len(trans)-1} transaction and you statement amount is {total_amt}')

# # cred_trans('mahesh',4322,57574,7585)

# # cred_trans('suresh',5634,7585,2533,8474)


# # Arbitrary Keyword Arguments.

# # ** -- for declaring the arbitrary keyword arguments..

# # def cred_trans(**trans):
# #     print(trans)
# #     total_amt = 0
# #     name = trans.pop('name')
# #     # print(trans)
# #     # print(name)
# #     for ele in trans:
# #         total_amt = total_amt + trans[ele]
# #     print(f'Hi {name},You have performed {len(trans)} transaction and you statement amount is {total_amt}')

# # cred_trans(jan=6467,feb=62272,name="suresh")

# # cred_trans(name="mahesh",mar=6474,april=8484,may=3838)

# # cred_trans(name="subash",jun=2332,july=7484,aug=4844,sep=9292)


# # def cred_trans(*trans,**trans_key):
# #     print(trans)
# #     print(trans_key)
# #     total_amt = sum(trans)
# #     print(f"Hi {trans_key['name']},you have performed {len(trans)} transactions for an amount of {total_amt} last month,we have sent an email to {trans_key['email']}")


# # print(cred_trans(6463,7478,7484,name="ramesh",email="ramesh@gmail.com"))


# # cred_trans(6463,6363,7478,7484,name="suresh",email="suresh@gmail.com")


# # return -- It will store the response and will send it to the function call and will move cursor directly to the function call..

# # def login_user(username,password):
# #     if username == 'suresh' and password=='suresh@123':
# #         return {'status':200,'message':"Logged in successful!"}
# #         print("Hello")
# #     else:
# #         return {'status':401,"message":"invalid login"}

# # print(login_user(input("enter username:"),input("enter password:")))

# # Local and Global varibales:


# # local varibales : Those which we can access only in the specific range itself.. inside the function only..
# # global varibales : Those which we can access anywhere through out the program..
# a=43

# def data(b,a):
#     global c
#     c=b
#     print(a)
#     print(b)

# data(9,15)

# print(a)
# print(c)


# Using a function inside other function.. -- higher order functions

# def domain_check(email):
#     # print(email)
#     if "@digital-lync.com" in email:
#         return {"status":'success'}
#     else:
#         return {'status':'invalid domain'}


# def login(email,password):
#     email1 = "sanjeeva@digital-lync.com"
#     password1 = 'password@123'
#     data_check = domain_check(email)
#     if data_check['status'] == 'success':
#         if email==email1 and password==password1:
#             return {"Message":"Logged in Success"}
#         else:
#             return {"Message":"Invalid credentials"}
#     else:
#         return data_check
# print(login('sanjeeva@digital-lync.com','password@123'))


# Recursion : A function calling itself..

# n! = n*(n-1)!
# 7! = 7*6!
#      7*6*5!
#      7*6*5*4*3*2*1!
#      7*6*5*4*3*2*1


# def cal_fact(a):
#     if a==1 or a==0:
#         return 1
#     else:
#         return a*cal_fact(a-1) # 7*6*5*4*3*2*1
    
# print(cal_fact(7))


# Lambda Functions or Anonymous Functions: A function which doesnot have any name..

# lambda -- it is the keyword for defining the lambda functions..

# syntax for lambda declaration
    # lambda arguments:expression


data = lambda a,b:a*b 

# print((lambda a,b:a*b)(4,5))

# print(data(3,4))


a=[32,54,13,54,64,84,21,75]

# final_data = []
# for ele in a:
#     final_data.append(ele+100)

# print(final_data)

# map -- for performing the logic for every element inside the sequence..

# print(list(map(lambda i:i+100,a)))

# filter()

# print(list(filter(lambda i:i%2==0,a)))

"""

Input:::
dict={
    "asaa":'asaa',
    "fsaf":"fsaf",
    "gagd":{
        "data":"data",
        "value":"value",
        "info":{
            "conpress":"compress",
            "product":"product",
            "data1":{
                "goon":"goon"
            }
        }
    },
    "sample":"sample"
    
}"""

"""
Output::
dict={
    "ASAA":'asaa',
    "FSAF":"fsaf",
    "GAGD":{
        "DATA":"data",
        "VALUE":"value",
        "INFO":{
            "COMPRESS":"compress",
            "PRODUCT":"product",
            "DATA1":{
                "GOON":"goon"
            }
        }
    },
    "SAMPLE":"sample"
    
}"""