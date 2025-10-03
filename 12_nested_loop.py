# nested loop  : a loop within a nother lop

#range(3) syntax can be used just for iteration prints 0,1,2
# but if iteraitons have to printed use range(1,4): prints 1,2 ,3
for x in range(3):
    for y in range(4):
        print(y,end="")
    print() #print(end="\n") default


rows = int(input("enter the number of rows : " ))
column = int(input("Enter the number of columns : "))
symbol = input("Enter the symbol to print : ")

for x in range(rows):
    for y in range(column):
        print(symbol,end="")
    print() #print(end="\n") default