# attributes : Varibales declared inside the class..

# 1) Instance attributes : Those attributes which are declared inside the self methods and can be accessed only with object.. 
# 2) Class Attributes : Those attributes which are declared outisde of all methods and inside class methods which can be accessed with only class and object(when we dont have any instance attribute with same name.)..

class Employee:
    name = "suresh"
    email = "suresh@gmail.com"

    def __init__(self,name,mobile): 
        self.name = name
        self.mobile = mobile

    def data(self):
        return self.name,self.email

# obj = Employee("ramesh","8787887654")

# # print(obj.name)
# # print(obj.mobile)

# print(Employee.name)
# print(obj.name) # 
# print(obj.email)