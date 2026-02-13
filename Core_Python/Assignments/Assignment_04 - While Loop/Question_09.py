# 9. WAP to print all numbers in a range divisible by a given number.

range=int(input("Enter a number :"))
num=int(input("Enter a divisibility number : "))

i=1
while(i<=range):
    if (i%num==0):
        print(i)

    i+=1