# Q.8 Write a program to convert days into years, weeks and day.

days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7
days_left = remaining_days % 7

print(f"{years} years, {weeks} weeks, {days_left} days")


