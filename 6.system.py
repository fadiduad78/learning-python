'''
create a menu where you can 
add student details
show how many students 
search student with roll number
to check unique subjects 
to delete student 
to check topper marks

and use if and else statments to 
to run the programm

*args






'''







students = {}


# ---------- Functions ----------

def add_student():
    roll = int(input("Enter Roll Number: "))
    
    if roll in students:
        print("Student already exists.")
        return
    
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    subjects = input("Enter Subjects (comma separated): ").split(",")

    # remove extra spaces
    subjects = [sub.strip() for sub in subjects]

    students[roll] = {
        "name": name,
        "age": age,
        "subjects": subjects
    }

    print("Student Added Successfully!\n")


def show_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    for roll, data in students.items():
        print(f"Roll No: {roll}")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Subjects: {', '.join(data['subjects'])}")
        print("-" * 20)


def search_student():
    roll = int(input("Enter Roll Number to Search: "))

    if roll in students:
        data = students[roll]
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Subjects: {', '.join(data['subjects'])}\n")
    else:
        print("Student not found.\n")


def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    if roll in students:
        del students[roll]
        print("Student Deleted.\n")
    else:
        print("Student not found.\n")


def unique_subjects():
    all_subjects = set()

    for data in students.values():
        for sub in data["subjects"]:
            all_subjects.add(sub)

    print("Unique Subjects:")
    print(", ".join(all_subjects))
    print()


def topper_check():
    print("Enter marks of 3 subjects:")

    m1 = int(input("Mark 1: "))
    m2 = int(input("Mark 2: "))
    m3 = int(input("Mark 3: "))

    marks = (m1, m2, m3)

    average = sum(marks) / len(marks)

    print("Average:", average)

    if average > 80:
        print("Topper\n")
    else:
        print("Needs Improvement\n")


# ---------- Main Program ----------

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Unique Subjects")
    print("6. Topper Check")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        unique_subjects()

    elif choice == "6":
        topper_check()

    elif choice == "7":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice\n")