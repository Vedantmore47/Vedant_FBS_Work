# Q.1  Write a program to calculte the percentage of student based on the marks of any 5 subjects .

maths=24
eng=50
sci=70
marathi=25
hindi=60

total=maths+eng+sci+marathi+hindi

percentage=(total/500) * 100

print("Percentage of student is ", percentage)


#__________________________________________________________________________________________________________________________


# Q.2 write a program to calculte the area of rectangle based on length and breadth 
length=100
breadth=50

area_of_rect=length*breadth
print("Area of rectangle", area_of_rect)

#__________________________________________________________________________________________________________________________


# Q.3 Program to find quotient and remainder of two numbers 

num1=30
num2=2

quotient= int(num1/num2) 
remainder= num1%num2

print("The Quotient is ",quotient ,"and Remainder is ", remainder)


#___________________________________________________________________________________________________________________________


#Q.4 Write a program to enter P, T, R and calculte the simple interest 

P= 1000
R=5
T=2

simple_Interest=(P*R*T)/100

print("The Simple Interest is ",simple_Interest)


#___________________________________________________________________________________________________________________________


#Q.5 Write a Program to enter P, T , R and calculate the compound interest 

P=1000
R=5
T=2

Amount=P*(1+R/100)**T
compound_interest=Amount-P

print("The Compound Interest is ", compound_interest)


#____________________________________________________________________________________________________________________________


# Q. 6 Write a Program to input two angles from user and find third angle of the triangle


angle1=30
angle2=60

angle3=180-(angle1+angle2)

print("Thirs angle is ",angle3)


#______________________________________________________________________________________________________________________________


# Q.7 Write a Program to find the roots of a quadratic equation 







# Q.8 Write a program to convert days into years, weeks and days.








# Q.9 Write a program to enter base and height of a triangle and find its area.

base=int(input("Enter the base :"))
height= int(input("Enter the height :"))
Area=0.5*base*height
print(f"the area of triangle is {Area}")


#__________________________________________________________________________________________________________________________________

#. Q.10. Write a program to calculate area of an equilateral triangle.
side = int(input("Enter the side of traingle :"))
Area_of_equi_tri=(1.732/4)*(side**2)
print(f"The area of equilateral triangle is {Area_of_equi_tri}")



#--------------------------------------------------------------------------------------------------------------------------------

# Q.11 Find the area and circumference of circle.
radius= int(input("enter the radius :"))
Area_of_circle=3.14*(radius**2)
print(f"The are of circle is {Area_of_circle}")

circumference=2*3.14*radius
print(f"The circumference of circle is {circumference}")


#----------------------------------------------------------------------------------------------------------------------------------


#.Q.12 Find the volume of sphere.
 
radius= int(input("enter the radius :"))
Area_of_sphere=(4/3)*3.14*(radius**3)
print(f"The are of circle is {Area_of_sphere}")

#------------------------------------------------------------------------------------------------------------------------------------













