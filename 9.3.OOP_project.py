class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self, name, age , grade ,roll_number):
        super().__init__(name, age)
        self.grade =grade
        self.roll_number = roll_number
        
    def show_details(self):
        super().show_details()
        print(self.grade)
        print(self.roll_number)
        print('--------------')
    

class Teacher(Person):
    def __init__(self, name, age , subject , salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    
    def show_details(self):
        super().show_details() 
        print(self.subject)
        print(self.salary)
        print('--------------')

        

class Staff(Person):

    def __init__(self, name, age , department , job_role):
        super().__init__(name, age)
        self.department = department
        self.job_role = job_role

    def show_details(self):
        super().show_details()
        print(self.department)
        print(self.job_role)
        print('--------------')

students = []

while True:
    print('1.Student Details')
    print('2.Teacher Details')
    print('3.Staff Details')
    print('4.Exit')

    choose = input('What you want to check choose (1 to 3) :')
    print('---------------------------------------------------')

    if choose == '1':

        name = input('Enter the name :')
        age = int(input('Enter the age :'))
        grade = input('Enter the Grade :')
        section = input("enter the Section: ")
        print('----------------------')
        
        s1 = Student(name , age , grade , section)
        students.append(s1)
        s1.show_details()

    elif choose == '2':

        name = input('Enter the name :')
        age = int(input('Enter the age :'))
        subject = input('Enter the Subject :')
        salary = input("enter your salary : ")
        print('----------------------')

        teacher = Teacher(name , age , subject , salary)
        teacher.show_details()

    elif choose == '3':

        name = input('Enter the name :')
        age = int(input('Enter the age :'))
        subject = input('Enter the department :')
        salary = input("enter your role : ")
        print('----------------------')

        staff = Staff('Azhar' , 35 , 'Computer Science' , 'Janitor' )
        staff.show_details()

    elif choose == '4':
        break
    else :
        print('Choose 1 to 3!')
        continue 


