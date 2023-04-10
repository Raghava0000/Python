# # datahiding : Providing the restrictions in accessing the attributes or methods from outside of the class.

# # Public Attributes -- Those which we can access anywhere without restrictions
# # Private Attributes -- Those which we can access only inside the class and child classes, not outside of the class.

# # Public Methods
# # Private Methods

# class Employee:
#     name = "Sanjeeva"
#     __address = "Hyderabad"

#     def __init__(self,email,mobile):
#         self.email = email
#         self.__mobile = mobile

#     def employee_info(self):
#         return f"{self.name} is from {self.__address} with mobile {self.__mobile}"

#     def __contact_info(self):
#         return f"you can contact {self.name} at {self.__mobile}"
    
#     def data(self):
#         return self.__contact_info()
        
# obj = Employee("sanjeev@gmail.com","7277382982")

# print(obj.employee_info())

# print(obj.name)
# # print(obj.__address)

# # obj-name._Classname__attribute-name
# print(obj._Employee__address)

# print(obj.data())

# print(obj.__contact_info())