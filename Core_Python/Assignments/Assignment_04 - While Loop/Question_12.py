# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)


num=int(input("Enter a number:"))

count=0

temp=num
sum=0

t=num
while(t!=0):
    count+=1
    t//=10

while(temp!=0):
    digit=temp%10

    mul=digit**count
    sum+=mul
    temp//=10




if(num==sum):
    print("It is armsrtong")
else:
    print("It is not armsrtong")


























