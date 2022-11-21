import random

word_list =  ["Qatar", "Ecuador", "Senegal", "Netherlands", "England", "Iran", "USA", "Wales", "Argentina", "Saudi Arabia", "Mexico", "Poland", "France", "Australia", "Denmark", "Tunisia", "Spain", "Costa Rica", "Germany", "Japan", "Belgium", "Canada", "Morocco", "Croatia", "Brazil", "Serbia", "Switzerland", "Cameroon", "Portugal", "Ghana", "Uruguay", "South Korea"]

#this function returns a random word from the word list & returns upper case to stop upper/lower case errors occuring later
def pick_word(word_list):
    word = random.choice(word_list)
    return word.upper()
    
#function to play game with chosen random word
def play_game(word):
    guessed_letter = []
    guessed_words = []
    