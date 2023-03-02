# Modules : Every Python file is a module..

# Modules are divided into 3 types:
    # Userdefined modules -- 
    # Built-in Modules
    # External Modules

# userdefined modules: Those modules which are created by user..

# import  -- Its the keyword for importing the module..

# 1st Syntax
    # import module-name 

import module1_cls

print(module1_cls.a)


# print(module1_cls.add(4,5))

# 2nd Syntax:

# from module-name import functionalities

# from module1_cls import *
# from module2_cls import *
# import module1_cls
# print(a)
# print(module1_cls.add(6,7))


# print(add(5,3))


# Python will check 3 path when it is loading the module..
    # Current Working directory..
    # Python Installed Location..
    # Python environment path are set..

# import sys

# sys.path.append("C:/Users/reddy/OneDrive/Documents")

# print(sys.path)

# from module2_cls import *

# print(add(5,3))

# datetime
# random
# urllib3.request 
# math

# from test_1 import test_123

# print(test_123.add(3,4))

