#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender=input("Enter a gender (M/F) :")
age=int(input("Enter an age :"))

if gender in ["m","M","Male","male","MALE"]:
    if age>=21:
        print("Eligible to marry")

    else:
        print("Not eligible ")

else:
    if age >=18:
        print("Eligible to marry")
        
    else:
        print("Not eligible ")
















