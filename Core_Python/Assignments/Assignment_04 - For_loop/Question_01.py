# 1. WAP to print all even numbers until n.

n=int(input("Enter a number:"))


#METHOD-1
for i in range(n+1):
    if(i%2==0):
        print(i)

#METHOD-2
for i in range(0,n,2):
    print(i)





