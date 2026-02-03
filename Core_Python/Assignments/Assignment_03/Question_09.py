# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

english=int(input("Enter a marks:"))
marathi=int(input("Enter a marks:"))
maths=int(input("Enter a marks:"))
science=int(input("Enter a marks:"))
hindi=int(input("Enter a marks:"))

total=english+marathi+maths+hindi+science
percentage=(total/500)*100
print("percentage =",percentage)

if(70<=percentage<=100):
    print("1st Class")

elif(50 <= percentage < 70):
    print("2nd Class")

elif (35 <=percentage <50):
    print("3rd class")
else:
    print("Fail")









