# logical operator ( and , or , not )

temp = int (input("what is the temperature outside??"))

if  temp >= 0 and temp <= 30:
    print("You can go outside .Cause the temperature is good.")
elif  temp < 0 or temp > 30 :
    print("Stay at home.")

"""
if not temp >= 0 and temp <= 30:
    print("You can go outside .Cause the temperature is good.")
elif not temp < 0 or temp > 30 :
    print("Stay at home.")

"""