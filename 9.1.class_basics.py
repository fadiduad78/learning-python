# class animal:
#     def speak(self):
#         print('It is an Animal')
# class dog(animal):   
#     def bark(self):
#         print('Woof Woof')   
    

# s1 = dog()
# s1.speak()
# s1.bark()


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Fahad", 18)
# s2 = Student('Ahmed', 19)

# print(s1.name ,' ',s2.name)
# print(s1.age ,'   ',s2.age)



class student():
    def __init__(self , name):
        self.name = name
    def greet(self):
        print(f'My Name is {self.name}!')
    
s1 = student('Fahad')
s1.greet()