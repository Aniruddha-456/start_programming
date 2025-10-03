# compuound intrest calculator  a=p(1+r/n) power t
import math

principle =0 
time = 0
rate = 0

while principle<=0 :
    principle = float(input("Enter the principal : "))
    if principle<=0 :
       print("No fella cant be 0")


#while True :
 #   principle = float(input("Enter the principal : "))
  #  if principle<=0 :
      #  print("No fellaaaaaa")
    ##else :
    #   break
    
    
while True :
    time = float(input("Enter the time : "))
    if time<=0 :
        print("No fella cant be 0")
    break

while True :
    rate = float(input("Enter the rate : "))
    if rate<=0 :
        print("No fella cant be 0")
    break

amount = principle * pow((1+rate/100),time)
print(f" the amount sums to {amount:.2f}")
