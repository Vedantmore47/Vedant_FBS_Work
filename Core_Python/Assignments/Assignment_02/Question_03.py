# 3. Convert distant given in feet and inches into meter and centimeter.

distance1=float(input("Enter a distance in feet :"))
distance2=float(input("Enter a distance in inches :"))

feet_to_meter=distance1*0.3048
inches_to_meter=distance2*39.3701


feet_to_centimeter=feet_to_meter*100
inches_to_centimeter= distance2*2.54


print("Conversion to Meter :")
print("Feet to meter :",feet_to_meter)
print("Inches to meter :",inches_to_meter)


print("Conversion to centiMeter :")
print("Feet to meter :",feet_to_centimeter)
print("Inches to meter :",inches_to_centimeter)


