import random
import time
import urllib
corrects = 0

def finish():
    yesList = ['y', 'yes', '1']
    noList = ['n', 'no', '2']
    print('\n --------------------------------------------------------------------------- \n')
    print("Would you like to play again?\n1) Y(Yes)\n2) N(No): ")
    playAgain = str(input())
    str(playAgain).lstrip()
    str(playAgain).lower()
    time.sleep(0.4)
    if playAgain in yesList:
        print('\n --------------------------------------------------------------------------- \n')
        introduction()
    elif playAgain in noList:
        print("Hope you enjoyed the game!")
        time.sleep(0.5)
    elif playAgain not in noList and playAgain not in yesList:
        print("Please enter a valid input!")
        finish()
    exit()

def win():
    print("Congratulations! You won!")
    print(f"The selected word was '{finalWord.title()}'\n")
    finish()

def man1():
    print(" -----")
    print("|    |")
    print("|    ")
    print("|    ")
    print("|   ")
    print("|    ")
    print("|   ")
    print("|________")

def man2():
    print(" -----")
    print("|    |")
    print("|    O")
    print("|    ")
    print("|   ")
    print("|    ")
    print("|   ")
    print("|________")

def man3():
    print(" -----")
    print("|    |")
    print("|    O")
    print("|    |")
    print("|   ")
    print("|    ")
    print("|   ")
    print("|________")

def man4():
    print(" -----")
    print("|    |")
    print("|    O")
    print("|    |")
    print("|   /|\\")
    print("|    ")
    print("|   ")
    print("|________")

def man5():
    print(" -----")
    print("|    |")
    print("|    O")
    print("|    |")
    print("|   /|\\")
    print("|   / \\")
    print("|________")

def checkGuess():
    global word, hearts, limit, wrongs, heartcount, display, corrects
    exitList = ['quit', 'exit']
    guess = input("Enter your guess: ")
    guess = guess.lstrip()
    guess = guess.lower()
    time.sleep(0.5)

    if guess in alreadyGuessed:
        print("Please enter a new guess!")
        checkGuess()

    elif guess in exitList:
        finish()

    elif guess in allowedlist and guess in word and guess not in alreadyGuessed and len(guess) == 1:
            alreadyGuessed.append(guess)
            corrects += 1
            if len(finalWord) == corrects:
                time.sleep(0.5)
                win()
            # places = ([pos for pos, char in enumerate(s) if char == c])
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            print(display + "\n")
            print(f"Great guess!      Hearts left : {hearts}")
            print (f"Here is the word: {display}")
            checkGuess()
    elif guess in allowedlist and guess not in word and len(guess) == 1:
        alreadyGuessed.append(guess) 
        wrongs = wrongs + 1
        heartcount = heartcount - 1
        hearts = "❤️ " * heartcount
        print (f"Unlucky! Wrong guess!     Hearts left : {hearts}")
        if wrongs == 1:
            man1()
            print (f"Here is the word: {display}")
        elif wrongs == 2:
            man2()
            print (f"Here is the word: {display}")
        elif wrongs == 3:
            man3()
            print (f"Here is the word: {display}")
        elif wrongs == 4:
            man4()
            print (f"Here is the word: {display}")
        elif wrongs == 5:
            time.sleep(0.5)
            man5()
            print("You have been hanged! Better luck next time!")
            print(f"The chosen word was '{finalWord.title()}'\n")
            finish()
        checkGuess()
        
        print(f"Here is the word: {display}")

    elif len(guess) > 1:
        print("Enter one character only.")
        checkGuess()

    elif guess not in allowedlist:
        print ("Enter English alphabetic characters only.")
        checkGuess()

    else:
        print("Unknown error")
        checkGuess()

def launch():
    global word
    global wordList
    global length
    global display
    global limit
    global wrongs
    global alreadyGuessed
    global allowedlist
    global heartcount
    global hearts
    global guess
    global displayList
    global finalWord
    word = random.choice(urllib.urlopen("https://sendeyo.com/en/e2a50a74df").read().split())
    wordList = list(word)
    finalWord = word
    length = len(word)
    display = "_" * length
    limit = 5
    wrongs = 0
    alreadyGuessed = []
    allowedlist = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    heartcount = limit - wrongs
    hearts = "❤️ " * heartcount
    print(f"Remaining Hearts : {hearts}")
    print(f"Here is the word: {display} (It's a {length}-letter word)")
    checkGuess()

def introduction():
    print("\n                  WELCOME TO THE HANGMAN GAME\n\n")
    time.sleep(0.5)
    print("=====================================================================\n")
    time.sleep(0.5)
    name = input("Please enter your name to start: ")
    time.sleep(0.5)
    print (f"Welcome to the game {name}! Enjoy!")
    print("1) Do not enter any characters other than english alphabetic characters. \n2) Enter one single letter at a time. \n3) Press control + c to force quit at any point. \n4) Type 'exit' or 'quit' to exit or restart the game.")
    time.sleep(1.5)
    launch()
introduction()