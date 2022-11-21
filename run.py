import random

word_list = ["Qatar", "Ecuador", "Senegal", "Netherlands", "England", "Iran", "USA", "Wales", "Argentina", "Saudi Arabia", "Mexico", "Poland", "France", "Australia", "Denmark", "Tunisia", "Spain", "Costa Rica", "Germany", "Japan", "Belgium", "Canada", "Morocco", "Croatia", "Brazil", "Serbia", "Switzerland", "Cameroon", "Portugal", "Ghana", "Uruguay", "South Korea"]

#this function returns a random word from the word list & returns upper case to stop upper/lower case errors occuring later
def pick_word():
    word = random.choice(word_list)
    return word.upper()
    
#function to play game with chosen random word
def play_game(word):
    #keeps track of the guessed letters & words
    guessed_letters = []
    guessed_words = []
    #keeps track of the game state
    guessed = False
    dashed_word = "_" * len(word)
    print("\n*****Welcome to the World Cup 22 Edition of Hangman!*****\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Try & guess the name of the team playing in the tournament")
    
    while not guessed and attempts > 0:
        guess = input("Kick-off by guessing a letter or word: ").upper() 
        if len(guess) == 1 and isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter, better change tactics!!", guess) 