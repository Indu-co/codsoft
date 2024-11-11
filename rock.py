import random

def get_computer_choice():
 choices = ["rock", "paper", "scissors"]
 return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
      return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
          (user_choice == "scissors" and computer_choice == "paper") or \
          (user_choice == "paper" and computer_choice == "rock"):
      return "user"
    else:
      return "computer"

def play_game():
  user_score = 0
  computer_score = 0
  play_again = "yes"
  print("Welcome to Rock-Paper-Scissors Game!")
  while play_again.lower() == "yes":
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
      print("Invalid choice. Please choose rock, paper, or scissors.")
      continue

    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
      print("It's a tie!")
    elif winner == "user":
      print("You win!")
      user_score += 1
    else:
      print("The computer wins!")
      computer_score += 1
      print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}")
      play_again = input("\nDo you want to play again? (yes/no): ").lower()
      print("\nThanks for playing! Final Score - You: {}, Computer: {}".format(user_score, computer_score))

play_game()