# exception : Nothing but errors..

# exception handlings : Handlings the errors.. 

# we use try and except :

"""
try:
    statements
except:
    statements
"""

# Inbuilt Exceptions
# Userdefined Exceptions

a=[23,6.7,'python',32,0,12.67]

# for ele in a:
#     try:
#         print(1/ele)
#     except:
#         print("error occured")


# for ele in a:
#     try:
#         print(1/ele)
#     except TypeError:
#         print("Type error occured")
#     except ZeroDivisionError:
#         print("Division with zero is not possible in programming")
#     except:
#         print("some error occured")
#     else:
#         print("Send email")

# Userdefined exceptions:

import random
class Smallvalueerror(Exception):
    pass

class Largevalueerror(Exception):
    pass

input1 = random.randint(100,200)

check=True
while check:
    try:
        input2 = int(input("Enter your input"))
        if input1 == input2:
            print("Number Guessed Correctly")
            # check=False
            break
        elif input2 > input1:
            raise Largevalueerror
        elif input2 < input1:
            raise Smallvalueerror
    except Smallvalueerror:
        print("Value entered is smaller, try with bigger value")
    except Largevalueerror:
        print("Value entered is greater , try with lesser value")