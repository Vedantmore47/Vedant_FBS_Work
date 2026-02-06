# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit=float(input("Enter a elctricity unit :"))



if (unit <=50):
    Total=unit*0.50 
    Total=Total+Total*20/100
    print(f"Toal bill is {Total}")

elif (51<= unit <= 150):
    Total=50 * 0.50 + (unit -50) *0.75 
    Total=Total+Total*20/100
    print(f"Toal bill is {Total}")

    

elif (151 <= unit <= 250):
    Total=50 * 0.50 + 100*0.75 + (unit-150) *1.20 
    Total=Total+Total*20/100
    print(f"Toal bill is {Total}")



elif(unit >=250):
    Total=50*0.50 + 100*0.75 + 100*1.20 + (unit-250)*1.50 
    Total=Total+Total*20/100
    print(f"Toal bill is {Total}")



    










