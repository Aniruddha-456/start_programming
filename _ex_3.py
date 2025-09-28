# lets write basic calculator program

op = input("Enter the operation (+,-,*,/) : ")
n1 = float(input("enter 1st number : "))
n2 = float(input("enter 2nd number : "))

if op == "+" :
    res = n1 + n2
    print(f"The addition of {n1} and {n2} is {res}")
elif op == "-" :
    res = n1 - n2
    print(f"The sub of {n1} and {n2} is {res}")
elif op == "/" :
    res = n1 / n2
    print(f"The div of {n1} and {n2} is {res}")
