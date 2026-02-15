# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.




user_id_OG="Vedant_more_47"
password_OG=18122004


for i in range(1,4):
    user_id=input("Enter a User ID :")
    password=int(input("Enter a password only in number :"))

    if(user_id== user_id_OG and password==password_OG):
        print("Your UserID and Password is correct !")
        break

    else:
        print("Your UserID and password is not correct !")


    if(i==3):
        print("SORRY...! , Code is terminated ")
        break






















