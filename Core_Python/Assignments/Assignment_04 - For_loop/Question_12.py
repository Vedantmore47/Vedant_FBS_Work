# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)


num=int(input("Enter a number:"))

temp=num
sum=0
count=0
i=1
t=num
while(t!=0):
    count+=1
    t//=10

while(temp!=0):
    digit=temp%10

    for i in range(1,digit+1):
        mul=digit**count

    sum+=mul
    temp//=10

print(sum)
if num==sum:
    print("It is armstrong number ")

else:
    print("It is not an armstrong")





















