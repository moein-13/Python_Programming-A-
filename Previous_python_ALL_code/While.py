"""
#########  while loop examples : ########


name = input ("Enter your name :")

while name == "":
    print("You didn't enter your name yet....")
    name = input("Enter your name :")

print(f"Hello {name}")


age = int(input("Enter your age :"))

while age < 0:
    print("Age can't be a negative no.")
    age = int(input("Enter your age :"))

print(f"Your age is {age}.")



food = input("Enter a name of food you like (q to quite) :")

while not food == "q":
    print(f"You like {food}.")
    food = input("Enter a name of food you like (q to quite) :")

print("babye.")

num = int(input("Enter a num between 1 to 10 :"))

while num < 1 or num > 10:
    print(f"{num} is not a valid one .")
    num = int(input("Enter a num between 1 to 10 :"))

print(f"The num is {num}.")

"""