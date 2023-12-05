import random

# Display the game instructions
print("Welcome to Rock, Paper, Scissors!")
print("The rules are simple:")
print("- Rock beats scissors")
print("- Scissors beats paper")
print("- Paper beats rock")
print("")

# Create a list of choices
choices = ["rock", "paper", "scissors"]

# Start the game loop
while True:
  # Get the player's choice
  player_choice = input("Choose rock, paper, or scissors: ")

  # Check if the player's choice is valid
  if player_choice not in choices:
    print("Invalid choice, please try again.")
    continue

  # Make the computer's choice
  computer_choice = random.choice(choices)

  # Display the choices
  print("You chose", player_choice)
  print("The computer chose", computer_choice)

  # Determine the winner
  if player_choice == computer_choice:
    print("It's a tie!")
  elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
  elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
  elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
  else:
    print("The computer wins.")
  
  # Ask if the player wants to play again
  play_again = input("Do you want to play again (y/n)? ")
  if play_again != "y":
    break

print("Thank you for playing!")
