import os


while True:
    print('1.Create File: ')
    print('2.Add Student: ')
    print('3.View Studets: ')
    print('4.Overrite File: ')
    print('5.Delete Files: ')
    print('6.Exit')
    
    choice = input('Enter a number : ')
    if choice == '1':
        if os.path.exists('student.txt'):
            print('file already exists')
        else:
          f = open('student.txt', 'x')
        print('File Created Successfully')
    elif choice == '2':
        name = input('Enter Name you Want to Write in File: ')
        with open('student.txt', 'a') as f:
            f.write(name + '\n')
            print(f'{name} , is Added to file')
    elif choice =='3':
        with open('student.txt' , 'r') as f:
            print(f.read())
    elif choice == '4':
        override = input('enter name to overwrite details : ')
        with open('student.txt', 'w') as f:
            f.write(override)
    elif choice == '5' :
        if os.path.exists("student.txt"):
            os.remove("student.txt")
            print("File deleted")
    elif choice == '6':
        break
        

""
"bank account system "
""
""

            


        
        
