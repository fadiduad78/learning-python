# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name)
#         print(self.age)
# s1 = Student('Ali',22)
# s1.show()

# # Inheritance
# # polymorphism
# # encapsulation


class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

s1 = Car(Vehicle)
