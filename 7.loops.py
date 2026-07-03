# cars = ("Civic", "BRV", "Corolla")

# for car in cars:
#     print(car)


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

print(topper_check())
