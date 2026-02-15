# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


num=int(input("Enter a number of passengers:"))

for i in range(1, num+1):
    print(f"PASSENGER {i}")
    age=int(input(f"Enter a age of passenger-{i}"))
    ticket_cost:100

    if(age<12):
        ticket_cost = ticket_cost - (ticket_cost*30)/100
        print("Ticket cost is",ticket_cost)

    elif(age>59):
        ticket_cost=ticket_cost-(ticket_cost*50)/100
        print("Ticket cost is",ticket_cost)

    else:
        ticket_cost=ticket_cost
        print("Ticket cost is",ticket_cost)


    total_ticket_cost+=ticket_cost    

print(f"Total ticket cost is {total_ticket_cost}")














