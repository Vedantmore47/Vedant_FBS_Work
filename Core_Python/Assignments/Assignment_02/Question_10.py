# 10. Write a program to reverse three-digit number.
num=int(input("Enter a number:"))

r1=num%10      #123--------->3
r2=num//10   #12

r3=r2%10    #2
r4=r2//10   #1

print(r1,r3,r4)