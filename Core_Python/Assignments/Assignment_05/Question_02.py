# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


num=int(input("Enter a number of students :"))
avg_percent=0
for i in range(1,num+1):
    print(f"STUDENT: {i}")
    eng=int(input("Enter a marks of English: "))
    maths=int(input("Enter a marks of Maths: "))
    sci=int(input("Enter a marks of Science: "))
    hindi=int(input("Enter a marks of Hindi: "))
    marathi=int(input("Enter a marks of Marathi: "))

    total=eng+maths+sci+hindi+marathi

    percent=total/500*100
    print(f"The percentage is {percent}")

    avg_percent+=percent

print(f"The Average percentage of {num} students is {avg_percent/num}")






