# 1. Convert the time entered in hh,min and sec into seconds.

hh=int(input("Enter a time in hours : "))
min=int(input("Enter a time in min : "))
sec=int(input("Enter a time in sec : "))


hh=hh*3600
min=min*60
sec=sec


result=hh+min+sec
print("total seconds :",result)






