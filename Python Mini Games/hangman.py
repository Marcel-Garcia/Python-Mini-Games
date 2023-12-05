import random

## Choose a random word from the list
#words = ["apple", "banana", "orange", "strawberry", "grapes", "kiwi", "mango", "pear", "pineapple", "watermelon"]

# Open the file and read the lines into a list
with open("words.txt", "r") as f:
  words = f.readlines()

# Strip the newline characters from the end of each word
words = [word.strip() for word in words]

# Choose a random word from the list
word = random.choice(words)

# Set the initial number of lives to 6
lives = 6

# Create a list of underscores the same length as the word
word_letters = ["_"] * len(word)

# Create a list of correctly guessed letters
guessed_letters = []

# Start the game loop
while True:
  # Print the current state of the game
  print("Current word:", " ".join(word_letters))
  print("Lives:", lives)
  print("Guessed letters:", " ".join(guessed_letters))

  # Get the player's guess
  guess = input("Enter a letter: ")

  # Check if the guess is valid
  if len(guess) != 1:
    print("Please enter a single letter.")
    continue
  elif not guess.isalpha():
    print("Please enter a letter.")
    continue
  elif guess in guessed_letters:
    print("You have already guessed that letter.")
    continue

  # Add the letter to the list of guessed letters
  guessed_letters.append(guess)

  # Check if the letter is in the word
  if guess in word:
    # Update the word_letters list to reveal the letter
    for i in range(len(word)):
      if word[i] == guess:
        word_letters[i] = guess
  else:
    # Decrement the number of lives
    lives -= 1

  # Check if the player has won or lost
  if "_" not in word_letters:
    print("Congratulations, you won!")
    print("The word was", word)
    break
  elif lives == 0:
    print("Sorry, you lost.")
    print("The word was", word)
    break

print("Thank you for playing!")
