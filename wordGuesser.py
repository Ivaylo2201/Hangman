import random


# Game restart
def newGame(userAnswer):
    if userAnswer.capitalize().strip() == "Yes":
        wordList.clear()
        usedLetters.clear()
        print()
        return True
    else:
        exit()


# Defining the possible words, the valid letters and 2 empty lists for future use.
wordsList = ["coin", "dog", "rose", "car", "climate", "bread", "earth", "friend", "fruit", "gold", "hotel", "juice",
             "lemon", "minute", "nature", "plane", "train", "space", "star", "air", "sound", "software", "art", "sun"
             "relax", "zebra", "bird", "sale", "twice", "wealth", "weather", "volume", "grass", "kiss", "look", "rich",
             "truck", "odd", "plant", "smartphone", "monitor", "bottle", "barrier", "doctor", "egg", "fitness",
             "minister"]

validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

usedLetters = []
wordList = []

while True:
    attempts = 10
    randomWord = random.choice(wordsList)

    for _ in range(len(randomWord)):
        wordList.append('*')

    print(' '.join(wordList))

    while True:
        # Checking if the user has reached the limit of attempts.
        if attempts <= 0:
            print(f"You ran out of attempts! The word was '{randomWord}'!")
            print()

            playAgain = input("Type 'Yes' to play again: ")
            if newGame(playAgain):
                break

        letter = input("Guess a letter: ")

        if letter not in validLetters or letter in usedLetters:
            print("Invalid letter or already used!")
            print()
            continue

        # Replace '*' with all instances of the letter if found.
        for i in range(len(randomWord)):
            if randomWord[i] == letter:
                wordList[i] = letter

        # Checking if the passed letter is in the selected word.
        if letter in randomWord:
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

                playAgain = input("Type 'Yes' to play again: ")
                if newGame(playAgain):
                    break
        else:
            attempts -= 1
            usedLetters.append(letter)
            if attempts > 0:
                print(f"Try another letter! {attempts} attempts left!")
            print()
