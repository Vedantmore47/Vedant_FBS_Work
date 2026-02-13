# 11. WAP to check if given number Strong Number.

num=int(input("Enter a number:"))  #123

temp=num

sum=0
while(temp!=0):
    digit=temp%10

    i=1
    fact=1
    while(i<=digit):
        fact*=i
        i+=1
        
    sum+=fact
    temp//=10



if(sum==num):
    print("It is a strong number ")

else:
    print("It is not a strong number ")

 