# 10. WAP to check if given number is Perfect Number.
# A perfect number is a number whose sum of proper divisors = the number itself.

num=int(input("Enter a number:"))

i=1
temp=num
sum=0
while(i<num):
    if(temp%i == 0):
        sum+=i
        print(i)
    i+=1

if(sum==num):
    print(f"{num} is a perfect number")

else:
    print(f"{num} is not a perfect number")


