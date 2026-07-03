def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def divid(x,y):
    return x/y

op = input("Chooses +   *  -  /  :")
x = float(input("Enter first Value x :"))
y = float(input("Enter second value y : "))

if op == "+":
    print("Answer x + y :", add(x,y))
elif op == "-":
    print("Answer x - y :", sub(x,y))
elif op == "*":
    print("Answer x * y :", mult(x,y))
elif op == "/":
    print("Answer x / y :", divid(x,y))
else :
    print("Not Valid")


