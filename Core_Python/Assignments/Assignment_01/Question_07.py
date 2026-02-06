# Q.7 Write a Program to find the roots of a quadratic equation 
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

d = (b*b) - (4*a*c)

r1 = (-b + d**0.5) / (2*a)
r2 = (-b - d**0.5) / (2*a)

print("Root 1 =", r1)
print("Root 2 =", r2)
