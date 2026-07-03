

from select import poll


student = {}


def add_student():
    
    roll = int(input("Enter the roll number: "))

    if roll in student:
           print("Roll No. Exists")
           return
        
    name = input('enter name : ')
    age = int(input('enter age : '))
    subjects = input('enter subjects : ')

    student[roll] = {
            'name' : name,
            'age' : age,
            'subjects' : subjects
        }

    
    print('Student Added!\n')

def show_students() :
    
    if len(student) == 0:
        print('No Students!')
        return
    
    """
    for key, value in dictionary.items()
    """
    for roll , data in student.items():
        print(f'Roll Number :{roll}')
        print(f'Name: {data["name"]}')
        print(f'Subjects: {data["subjects"]}')
        print("-"*20)

def search_roll() :
    roll = int(input('Enter Roll Number : '))
    
    if roll in student:
        data = student[roll]
        print(f'Roll Number :{roll}')
        print(f'Name: {data["name"]}')
        print(f'Subjects: {data["subjects"]}')
        print("-"*20)
    else:
        print('student not found')

    

while True:
    print('\n1.Add Student')
    print('2.Show Number of students')
    print("3.Exit")


    choice = input('Enter Choice 1 or 2:  ')

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        break
    else:
        print('Choose 1 or 2\n')

    
    



    









    
