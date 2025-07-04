import random

def get_user_choice():
    choice = input("Enter your choice (rock,paper,scissor): ").lower()
    while choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Try again.")
        choice = input("Enter your choice (rock, paper, scissor: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissor"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

#main game loop
def play():
    print("Welcome to rock-Paper-Scissor!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

#Run the game
play()                 

