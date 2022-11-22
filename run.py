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
    #replaces word with same amount of dashes as letters in word
    dashed_word = "_" * len(word)
    #max attempts player has to guess word
    attempts = 6
    print("\n*****Welcome to the World Cup 22 Edition of Hangman!*****\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Try & guess the name of the team playing in the tournament")
    
    while not guessed and attempts > 0:
        guess = input("Kick-off by guessing a letter or word: ").upper() 
        if len(guess) != 1:
            print('Please enter a single letter. YELLOW CARD!!')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        elif guess in guessed_letters:
            print("You already guessed this LETTER, better change tactics!!", guess)
        elif guess in guessed_words:
            print("What a miss!! You already guessed this WORD!!", guess)
        elif guess not in word:
            print(guess, "is not in the word.") 
            attempts -= 1
            guessed_letters.append(guess)
        else:
            print("GGGGGOAL,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(dashed_word)
            indices = [i for i, letter in enumerate(word) if letter == guess]             
            for index in indices: 
                word_as_list[index] = guess 
            dashed_word = "".join(word_as_list) 
            if "_" not in dashed_word: 
                guessed = True     
        print(display_hangman(attempts)) 
        print(dashed_word) 
        print("\n")
    
    if guessed: 
        print("RESULT!!! You have won the match & guessed the word correctly! Olé Olé Olé...")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
    
    def display_hangman(attempts):
        
