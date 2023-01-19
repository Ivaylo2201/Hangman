# Importing random library for future use.
import random


# Defining a function to check if the user wants to play again.
def playAgain(ans):
    usedLetters.clear()
    wordList.clear()

    if ans.lower() == "yes":
        return True
    elif ans.lower() == "no":
        return False


def exitFunc():
    print()
    print("Goodbye!")
    print("Hangman made by Ivaylo Georgiev.")
    exit()


# Defining the possible words, the valid letters and 2 empty lists for future use.
wordsList = ["coin", "dog", "rose", "car", "climate", "bread", "earth", "friend", "fruit", "gold", "hotel", "juice",
             "lemon", "minute", "nature", "plane", "train", "space", "star", "air", "sound", "software", "art", "sun"
             "relax", "rich", "zebra", "bird", "sale", "twice", "wealth", "weather", "volume", "grass", "kiss", "look",
             "truck", "odd", "plant", "smartphone", "monitor", "bottle", "barrier", "doctor", "egg", "fitness", "minister"]

validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

usedLetters = []
wordList = []

while True:
    attempts = 10
    # Generating one random number from 0 to the length of wordsList.
    randomNum = random.randint(0, len(wordsList) - 1)

    # Taking away the word on the generated number.
    randomWord = wordsList[randomNum]

    # Putting '*' instead of the length of the word.
    for _ in range(len(randomWord)):
        wordList.append('*')
    print()

    # Printing the number of letters in the word without revealing them.
    print('* ' * len(randomWord))

    while True:
        # Checking if the user has reached the limit of attempts.
        if attempts <= 0:
            print(f"You ran out of attempts! The word was '{randomWord}'!")
            print()

            x = input("Do you want to play again? [Yes / No] -> ")
            if playAgain(x):
                break
            else:
                exitFunc()

        # Asking the user for a letter.
        letter = input("Guess a letter: ")

        # Replace '*' with all instances of the letter if found.
        for i in range(len(randomWord)):
            if randomWord[i] == letter:
                wordList[i] = letter

        # Checking if the input is valid
        if letter not in validLetters or letter in usedLetters:
            print("Invalid letter or already used!")
            print()
            continue

        # Checking if the prompted letter is in the selected word.
        if letter in randomWord:
            # Saving the letter, so the user can not use it again.
            usedLetters.append(letter)

            ind = randomWord.index(letter)
            wordList[ind] = letter

            print(' '.join(wordList))
            print()

            # Checking if the user revealed all the letters (Guessed the word).
            if '*' not in wordList:
                guessedWord = ''.join(wordList)
                print(f"Congratulations! You guessed the word!")
                print(f"It was: '{guessedWord}'")
                print()

                # Asking the user whether they want to play again.
                x = input("Do you want to play again? [Yes / No] -> ")
                if playAgain(x):
                    break
                else:
                    exitFunc()
        else:
            # Take out 1 of the attempts, save the letter and print the remaining attempts.
            attempts -= 1
            usedLetters.append(letter)
            if attempts > 0:
                print(f"Try another letter! {attempts} attempts left!")
            print()
