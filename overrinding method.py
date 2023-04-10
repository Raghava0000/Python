# Polymorphism : Multiple forms of writing the methods

    # Method overriding
    # Method overloading

# Method overiding : Considering the child class method only even though we have the parent clas method with same name..

class Father:
    acres = 12 
    location = "Kurnool"

    def property_info(self):
        return f"You have {self.acres} of land at {self.location}"


class Child(Father):
    # acres = 5 
    location = "Hyderabad" # class attributes

    def property_info(self):
        return f"In {self.location} you have {self.acres} acres of agriculture land."

# obj = Child()

# print(obj.acres)

# print(obj.property_info())

# Method Overlaoding: 