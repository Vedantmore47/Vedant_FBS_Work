# 7. Write a program to check if user has entered correct userid and password.

userid=input("Enter UserID :")
password=input("Enter Password:")


if (userid.isalnum()) and (len(userid)==6):
    print(f"{userid} is valid.")
else:
    print(f"{userid} is not valid ")

if (len(password)>=8) and (not password.isalnum()) :
    print("password is valid ")

else:
    print("password is not valid")




# isalnum() checks whether a string contains only letters and numbers.
#ALNUM = ALPHABET + NUMBER

# Letters → a–z, A–Z
# Numbers → 0–9

# Returns:
# True → if string has only alphabets and digits
# False → if string has any space or special character


