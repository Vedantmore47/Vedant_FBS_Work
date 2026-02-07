# 7. Find the sum of three-digit number.

num=int(input("Enter a 3-digit number:"))

r1=num%10      #123 -----> 3
r2=num//10     #123//10---->12

r3=r2%10        # 12%10 ---> 2
r4=r2//10       #12//10 ---->1


print(r1+r4+r3)