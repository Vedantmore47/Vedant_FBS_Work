# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1=float(input("Enter a side1:"))
side2=float(input("Enter a side2:"))
side3=float(input("Enter a side3:"))

if  (side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
    if(side1==side2==side3):
        print("Triangle is equilateral")
    elif (side1==side2 or side2==side3 or side3 ==side1 ):
        print("Triangle is Isosceles")
    else:
        print("Triangle is scalene")
else:
    print("Triangle is not valid")






