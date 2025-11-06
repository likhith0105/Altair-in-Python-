import math
a = int(input("enter the  number"))
sqrtt = math.sqrt(a)
sqrtt = math.floor(sqrtt)
square = sqrtt * sqrtt
if (a == square):
    print("perfect square")
else:
    print("not a perfect square")    

#leap year
a = int(input("enter the year:"))
if(a % 400==0):
    print("leap year")
elif (a % 4==0 and a %100!=0):
    print("leap year")
else:
    print("not a leap year")    


#postive or negative
a=int(input("enter a number:"))
if(a>0):
    print("the number is positive!!!")
elif(a<0):
    print("the number is negative!!!")
else:
    print("the number is zero!!")


from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h=0
for i in range(75):
    color(hsv_to_rgb(h,1,1))
    h+=0.014
    right(1)
    forward(1)
    for j in range(3):
        right(2)
        circle(150)
        hideturtle()
done()