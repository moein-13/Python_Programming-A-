
import random

print("### NUMBER GUESSING GAME ###")

num = input("\nType a number : ")

if num.isdigit():
    num = int(num)

    if num <= 0:
        print("Please type a Number larger than 0 .")
        quit()

    #else:
    #    print("please type a Number next time. ")

random_num = random.randrange(0,num)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess : ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type a num next time .")
        continue

    if user_guess == random_num:
        print("You got it !!")
        break

    elif user_guess > random_num:
        print("You were above the num.")
    else:
        print("You were below the num .")

print("You got it in ", guesses , "guesses.")