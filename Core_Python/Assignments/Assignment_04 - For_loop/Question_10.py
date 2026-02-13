# 10. WAP to check if given number is Perfect Number.
# A perfect number is a number whose sum of proper divisors = the number itself.

num=int(input("Enter a number :"))
sum=0

for i in range(1,num):

    if(num % i==0):
        sum+=i

print(sum)

if(sum==num):
    print("It is perfect number ")

else:
    print("It is not perfect number ")














