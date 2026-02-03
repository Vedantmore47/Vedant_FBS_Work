# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not. 

side1=float(input("Enter a side 1:"))
side2=float(input("Enter a side 2:"))
side3=float(input("Enter a side 3:"))


if (side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
    print("Traingle is valid ")
    
else:
    print("Triangle is not valid")
    






