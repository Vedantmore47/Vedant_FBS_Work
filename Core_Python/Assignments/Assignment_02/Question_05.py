# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price=float(input("Enter a cost_price :"))
discount=int(input("Enter a discount :"))

selling_price=cost_price-(discount *cost_price)/100

print("Selling price of book is ", selling_price)