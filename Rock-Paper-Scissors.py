print("Rules of Rock, Paper, Scissors\nRock beats Scissors!\nScissors beats Paper\nPaper beats Rock!\nLet's Play!!!")
user_name = input("Bot wanna know your name- ")
while True:
    import random
    user_choice = input("What do you wanna play?\nRock\t Paper\t Scissors! ")
    possible_choices = ["Rock", "Paper", "Scissors"]
    bot_choice = random.choice(possible_choices)
    print(f"\n{user_name} played {user_choice} and Bot played {bot_choice}.\n")
    if user_choice == bot_choice:
        print(f"\n{user_name} and Bot both played {user_choice}.\nIt's a tie!")
    elif user_choice == "Rock":
        if bot_choice == "Paper":
            print("\nYaay! Bot wins!")
        else:
            print(f"\nHurray! {user_name} wins!")   
    elif user_choice == "Paper":
        if bot_choice == "Scissors":
            print("\nYaay! Bot wins!")
        else:
            print(f"\nHurray! {user_name} wins!") 
    elif user_choice == "Scissors":
        if bot_choice == "Rock":
            print("\nYaay! Bot wins!")
        else:
            print(f"\nHurray! {user_name} wins!")
    if input("\nWanna play again? Y/N ") == "N":
        break