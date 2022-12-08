import random

while True:
    user = input("Enter rock, paper, scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    python = random.choice(possible_actions)
    print(f"\nYou chose {user}, computer chose {python}.\n")

    if user == python:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if python == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if python == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if python == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
