# Validate user input
# username : not more than 12 chars, must not contain spaces and digits

name = input("Enter your name : ")

#if len(name) > 12 or name.count(" ") == True or name.isalpha() == False :
 #   print("Thats invalid")

#lse : 
 #   print("great")


#alternate code

if len(name) > 12:
    print("not valid fellow ")
elif name.find(" ") != -1:
    print(" no spaces mate")
elif not name.isalpha() :
    print("no digits folk")
else : 
    print(f"Your username is {name}")