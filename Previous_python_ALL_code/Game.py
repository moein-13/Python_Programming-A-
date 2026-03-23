import random

print("Winning Rules of the Game ROCK PAPER SCISSORS are : \n"
      + "Rock vs Paper --> Paper wins \n"
      + "Rock vs Scissors --> Rock wins \n"
      + "Paper vs Scissors --> Scissors wins \n")

while True:
    print("Here's YOUR choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    # input validation loop
    while True:
        try:
            choice = int(input("Enter Your choice: "))
            if 1 <= choice <= 3:
                break
            else:
                print("Enter a valid choice (1-3)...")
        except ValueError:
            print("Please enter a number between 1 and 3.")

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    print("\nUser choice is:", choice_name)
    print("\nNow it's computer's turn.")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    print("\nComputer choice is:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    #  win condition logic
    if choice == comp_choice:
        result = "Draw"
    elif (choice == 1 and comp_choice == 3) or \
         (choice == 2 and comp_choice == 1) or \
         (choice == 3 and comp_choice == 2):
        result = "User"
    else:
        result = "Computer"

    if result == "Draw":
        print("\n$$ It's a tie $$")
    elif result == "User":
        print("\n## User wins! ##")
    else:
        print("\n@@ Computer wins. @@\n")

    print("\nDo You want to play again? (Y/N)\n")
    ans = input().lower()
    if ans == 'n':
        break

print("\nTHANKS FOR PLAYING.")