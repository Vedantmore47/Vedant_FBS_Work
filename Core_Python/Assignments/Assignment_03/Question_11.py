# 11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.


person1=int(input("Enter a age:"))
person2=int(input("Enter a age:"))
person3=int(input("Enter a age:"))
person4=int(input("Enter a age:"))
person5=int(input("Enter a age:"))

ticket_amount=100
total_amount=0
#person-1
if (person1<12):
    total_amount_1=ticket_amount-(ticket_amount*(30/100))

elif (person1>59 ):
    total_amount_1=ticket_amount-(ticket_amount*(50/100))

else:
    total_amount_1=ticket_amount
    
#PERSON-2
if (person2<12):
    total_amount_2=ticket_amount-(ticket_amount*(30/100)) + total_amount_1

elif (person2>59 ):
    total_amount_2=ticket_amount-(ticket_amount*(50/100))+ total_amount_1

else:
    total_amount_2 = ticket_amount +total_amount_1


#PERSON-3
if (person3<12):
    total_amount_3=ticket_amount-(ticket_amount*(30/100))  + total_amount_2

elif (person3>59 ):
    total_amount_3=ticket_amount-(ticket_amount*(50/100)) + total_amount_2

else:
    total_amount_3=ticket_amount+total_amount_2
    


#person -4
if (person4<12):
    total_amount_4=ticket_amount-(ticket_amount*(30/100))  +total_amount_3

elif (person4>59 ):
    total_amount_4=ticket_amount-(ticket_amount*(50/100)) + total_amount_3

else:
    total_amount_4=ticket_amount + total_amount_3


#PERSON-5 
if (person5<12):
    total_amount_5=ticket_amount-(ticket_amount*(30/100))  + total_amount_4

elif (person5>59 ):
    total_amount_5=ticket_amount-(ticket_amount*(50/100)) + total_amount_4

else:
    total_amount_5 =ticket_amount +total_amount_4


print(total_amount_5)




