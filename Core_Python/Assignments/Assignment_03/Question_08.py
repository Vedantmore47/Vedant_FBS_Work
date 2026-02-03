# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random 
userid=input("Enter a UserID :")
password=input("Enter a password :")

if (userid.isalnum() and len(userid)==6) and ( not password.isalnum() and len(password)>=8 ):
    print("userid and password is correct ")
    num=random.randint(1000,9999)
    print(num)

    random_num=int(input("Enter a number : "))
    if (random_num== num):
        print("Succesfull !")
    else:
        print("not successfull ...")

else:
    print("userid and password is incorrect")









