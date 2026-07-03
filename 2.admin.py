password = ""
while password != "admin" :
    password = input("Enter Password: ")


print("You Entered The Calculator")



op = input("Choose:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n:")

if op == "1":
    x = float(input("Enter Value X :"))
    y = float(input("Enter Value Y :"))
    print(f"Your Answer :", x+y)
elif op == "2" :
    x = float(input("Enter Value X :"))
    y = float(input("Enter Value Y :"))
    
    print(f"Your Answer :", x-y)
elif op == "3" :
    x = float(input("Enter Value X :"))
    y = float(input("Enter Value Y :"))
    print(f"Your Answer :",x*y )
elif op == "4" :
    x = float(input("Enter Value X :"))
    y = float(input("Enter Value Y :"))
    
    print(f"Your Answer :", x/y)
else :
    print("Select 1 to 4")