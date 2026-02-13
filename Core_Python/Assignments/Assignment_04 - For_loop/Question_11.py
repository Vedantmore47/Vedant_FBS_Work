# 11. WAP to check if given number Strong Number.
#Example: 145 =1! + 4! + 5!

num=int(input("Enter a number:"))


sum=0
temp=num
while(temp!=0):
    
    digit=temp%10
    
    fact=1

    for i in range(1,digit+1):
        fact*=i


    sum+=fact
    temp//=10

print(sum)

if(num==sum):
    print("It is strong number")

else:
    print("It is not a strong number ")
    



























