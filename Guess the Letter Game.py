import random
import time

print("Welcome to the Letter Guessing Game by Mayank Parekh.")
print("Hope you have fun!!!")

# Input for number of players
players = input("Enter the number of players: ")
while not players.isdigit():
    print("You have entered an invalid number.")
    players = input("Enter the number of players: ")
players = int(players)

# Input for number of rounds to win
winner_rounds = input("The overall winner has to win how many rounds?: ")
while not winner_rounds.isdigit():
    print("You have entered an invalid number.")
    winner_rounds = input("The overall winner has to win how many rounds?:")
winner_rounds = int(winner_rounds)

winnings = [0] * players  # Store the number of winnings by each player
nameList = []  # Store the names of the players

# Creating the list for all the players
for i in range(players):
    name = input(f"Enter player {i + 1} name: ")
    nameList.append(name)

# Function to remove a random letter from a word
def remove_random_letter(word):
    index = random.randint(0, len(word) - 1)
    return word[:index] + word[index+1:], word[index]

# Function to play the letter guessing game
def guess_the_letter():
    round = 1  # Initialize round counter
    while True:  # Game runs until a winner is found
        print(f"\n--- Round {round} ---")
        
        # Loop through each player
        for playerNumber in range(players):
            guessCount = 0  # Number of guesses by the current player
            
            # Generate a random word
            words = ['python', 'programming', 'developer', 'algorithm', 'computer', 'random']
            word = random.choice(words)
            modified_word, missing_letter = remove_random_letter(word)

            print(f"Word with a missing letter: {modified_word}")

            # Player guesses the missing letter
            guess = input(f"Player {nameList[playerNumber]} - Guess the missing letter: ").strip().lower()
            guessCount += 1

            # Check if the guess is correct
            if guess == missing_letter:
                print("Correct! Well done!")
                winnings[playerNumber] += 1  # Update winnings
                print("-" * 15 + "Congratulations!!!" + "-" * 15)
                print(f"{nameList[playerNumber]}, you made the right guess!")
                print(f"The missing letter is: {missing_letter}")
            else:
                print(f"Wrong! The missing letter was '{missing_letter}'.")

            # Display the winnings after each round
            for i in range(players):
                print(f"{nameList[i]} - Total number of wins: {winnings[i]}")
            
            # Check if any player reached the required number of wins
            maxWin = max(winnings)
            if maxWin >= winner_rounds:
                winPlayer = winnings.index(maxWin)
                print(f"HURRAY! The overall winner is {nameList[winPlayer]}")
                return  # Exit the game after a winner is found
        
        round += 1  # Increment round counter

# Run the game
guess_the_letter()

print("\nThanks for playing!")
print("Signed off, Mayank...")
time.sleep(5)
