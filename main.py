import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["R", "P", "S"]
    computer_action = random.choice(possible_action)
    print(f"\n You chose {user_action}, computer chose {computer_action}.\n ")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win.")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "rock":
            print("Paper covers rock! You win.")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "paper":
            print("Scissors cuts paper! You win.")
        else:
            print("Rock smashes Scissors! You lose.")
    else:
        print("ERROR")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

