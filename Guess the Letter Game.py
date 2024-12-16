import random

def remove_random_letter(word):
    index = random.randint(0, len(word) - 1)
    return word[:index] + word[index+1:], word[index]

def guess_the_letter():
    words = ['python', 'programming', 'developer', 'algorithm', 'computer', 'random']
    word = random.choice(words)
    modified_word, missing_letter = remove_random_letter(word)

    print(f"Word with a missing letter: {modified_word}")

    guess = input ("Guess the missing letter: ").strip().lower()

    if guess == missing_letter:
        print ("Correct! Well done!")

    else:
        print (f"Wrong! The missing letter was '{missing_letter}'.")

        # Run the game
guess_the_letter()





             
             