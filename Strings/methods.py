# methods:-strtswith, endswith, islower, isupper, lower, upper, isalpha, isalnum, capitalize, title, swapcase, count, index, find, split,strip, join, replace, zfill, farmat().
# 1)startswith:-
# sample="Django is a python framework"
# print(sample.startswith('D'))   # true
# print(sample.startswith('d'))   # false
# print(sample.startswith('Djan'))   # true

# 2)endswith:-
# sample="Django is a python framework"
# print(sample.endswith('k'))  #true
# print(sample.endswith('o'))  #false
# print(sample.endswith('work'))  #true

# 3)islower:-will check whether all characters are in lowercase
# sample="Django is a python framework"
# print(sample.islower())  #false

# sample1="django is a python framework"
# print(sample1.islower())  #true

# 4)isupper:-will check whether all characters are in uppercase
# sample="Django is a python framework"
# print(sample.isupper())

# sample="DJANGO IS PROGRAMMING LANGUAGE@123"
# print(sample.isupper())


# 5)lower:-
# sample="Django is a Python Framework"
# print(sample.lower())


# 6)upper:-
# sample="Django is a python framework"
# print(sample.upper())


# 7)isalpha:-it will check whether everything inside the string is alphabet or not
# sample="JaiBalayyaVeeraSimhaReddy"
# print(sample.isalpha())   #true

# sample1="Jai Balayya Veera Simha Reddy"
# print(sample.isalpha())   #false


# 8)isalnum:-it will check whether everything inside the string is alphabet or number
# sample="JaiBalayyaVeeraSimhaReddy"
# print(sample.isalnum())  #true

# sample="JaiBalayyaVeeraSimhaReddy 1123"
# print(sample.isalnum())  #false

# sample1="123"
# print(sample1.isalnum())   #true


# 9)isdigit:-it will check whether everything inside the string is no.s only
# sample="963852741"
# print(sample.isdigit())     #true

# sample1="963321741AXN"
# print(sample1.isdigit())    #false

# 10)title:-each and everyword starting letter changes to capital
# sample="Jai balayya, Jai jai Balayya"
# print(sample.title())


# 11)capitalize:-starting word change ti capital
# sample="Jai balayya, Jai jai Balayya"
# print(sample.capitalize())


# 12)swapcase:-uppercase changes to lowercase
# sample="Jai balayya, Jai jai Balayya"
# print(sample.swapcase())


# 13)index:-it will return the index value of the element inside the string(it will give 1st occurance)
# sample="Jai balayya, Jai jai Balayya"
# print(sample.index('y')) 
# print(sample.index('b')) 
# print(sample.index('a')) 

 
# 14)rindex:-it will return the index value of the element inside the string with starts it from rightside
# sample="Jai balayya, Jai jai Balayya"
# print(sample.rindex('B'))
# print(sample.rindex('a'))


# 15)find:-it will return the index value of the element inside the string (will give the 1st occurance)
# sample="Jai Balayya Jai Jai Balayya"
# print(sample.find('y'))
# print(sample.find('a'))
# print(sample.find('i'))
# print(sample.index(''))
# print(sample.find(''))



# 16)count:-it will return the count of how many times the substring is occured inside the main string
# sample="Jai Balayya Jai Jai Balayya"
# print(sample.count('B'))
# print(sample.count('jai'))


# 17)split:-it will splits the words separately like as strings in list..
# sample="Jai Balayya Jai Jai Balayya"
# print(sample.split())
# print(sample.split('Ba'))
# print(sample.split('z'))

# 18)rsplit:-
# sample="Jai Balayya Jai Jai Balayya"
# print(sample[0:5].rsplit('a'))
# print(sample[0:10].rsplit('a'))


# 19)strip:-its for removing the escae sequences at the starting and ending of the string
# sample="@\nJai\t Balayya \n Jai\t Jai\t Balayya\n"
# print(sample.strip())
# print(sample.strip())

# 20)rstrip:-
# print(sample.rstrip())
# print(sample.lstrip('@))



# 21)zfill:-its for filling up with 0's
# a="8529637"
# print(a.zfill(12))



# 22)replace:-replace the substring in other substring
# dialogue="dont trouble the trouble if you trouble the trouble trouble troubles you i am not trouble i am the truth "
# print(dialogue.replace("trouble","problem"))
# print(dialogue.replace("trouble","problem",3))


# 23)join:-its for join a substring to the each character in the main string
# name="Python"
# print(" ".join(name))

# names=["python,django,fullstack,devops"]
# print(" ".join(names))

# name1="django"
# name2="fullstack"
# name3=[name1,name2]
# print(" ".join(name3))
# print(name1+ " " +name2)


# 24)format():-
# message="use this otp 852030 for the amount of Rs.40500 for your transaction at amazon"
# otp=input("enter otp :")
# amount=input("enter amount :")
# website=input("enter website :")

# message="use this otp {} for the amount of rs.{} for your tranction at {}.".format(otp,amount,website)
# # latest version farmat::
# message=f"use this otp {otp} for the amount of Rs.{amount} for your tranction at {website}."

# print(message)



# eg:data is..
pin1=1234
account_type1="savings"

pin2=int(input("enter your pin :"))
if pin1 == pin2:
    account_type2=input("enter account type")
    if account_type1 == account_type2:
        amount=input("enter amount :")
        print(amount,"is debited from your account")
    else:
        print("account does not matched")        
else:
    print("invalid pin")



