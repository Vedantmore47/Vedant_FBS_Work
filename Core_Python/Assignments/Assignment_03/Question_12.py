# 12. Write a program to check if given 3 digit number is a palindrome or not.

num=int(input("Enter a 3 digit number :")) #123

n1=num%10     #3
n2=num//10    #12

n3=n2//10      #2



if(n1==n3):
    print("The number is palindrome")

else:
    print("The number is not Palindrome")













