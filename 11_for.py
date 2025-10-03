# for loop: execute a block of code a fixed number if times 


for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)


for x in range(1,5):
    if x == 3:
        continue
    else:
        print(x)

for x in range(1,5):
    if x == 3:
        break
    else:
        print(x)