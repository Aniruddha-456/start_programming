
name = input("enter your name : ")

while name == "":
    print("Cant be empty fellow")
    name = input("enter your name again : ")

print(f"name is {name}")

age = int(input("Enter your age : "))

while age<0:
    print("Cant be -ve fellow")
    age = input("enter your age again : ")

print(f"age is {age} ")


food = input(" what u want (q to quit): ")

while food!="q":
    print(f"food is {food} ")
    food = input(" what u want (q to quit): ")
    
