## In tupples we can not change anything in the variables
"""
cordinates = [(4 , 5) , (9,2),(11,33)]
cordinates [1] = [(2 , 9)] ## But if we use element in the first parantheses into the third parentheses
print(cordinates[1])

mytuple = (1,1,2,3,3,434,4)
print(mytuple)"""
students = ("Moein" , 22 , "Male","Male")

#print(students.index("Moein"))
#print(students.count("Male"))


for i in students:
    print(i)
print()

if "Moein" in students:
    print("Moein is here !!!")
