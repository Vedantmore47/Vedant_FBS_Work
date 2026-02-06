#Q.5 Write a Program to enter P, T , R and calculate the compound interest 

P=1000
R=5
T=2

Amount=P*(1+R/100)**T
compound_interest=Amount-P

print("The Compound Interest is ", compound_interest)