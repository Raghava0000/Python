# Methods: Functions declared inside the class are called methods 

# 1) Instance methods : Those methods which we can access only with object name.. and which contains self as default argument.
# 2) Class Methods : Those methods which can be access with bpth clas and object and which take cls as default arguments
# 3) Static methods : Those methods which can be access with bpth clas and object and which doesnot take any attribute..

class Employee:
    name = "venkatesh"

    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    def info(self,address):
        self.address = address
        return f"HI {self.name}, your email id is {self.email} and address {address}"

    def address_info(self):
        return f"Hi {self.name} your address is {self.address}"

    @classmethod
    def cls_info(cls,email):
        cls.email = email
        return f"{email} is registered under {cls.name} user."

    @classmethod
    def cls_email_send(cls):
        return f"Email has been sent to {cls.email}"

    @staticmethod
    def static_email_send(email):
        return email
    
obj = Employee("mahesh","mahesh@gmail.com")

# print(obj.name)

# print(obj.info("Hyderabad"))

# print(Employee.info())

# print(obj.address_info())

print(obj.cls_info('venkatesh@gmail.com'))

print(Employee.cls_info('venkatesh@gmail.com'))

print(obj.cls_email_send())

print(obj.static_email_send('mahesh@gmail.com'))

print(Employee.static_email_send('mahesh@gmail.com'))