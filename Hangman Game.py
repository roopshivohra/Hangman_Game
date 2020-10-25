#hangman game
""""import random,time
fruits=['pear','mango','apple','banana','apricot','pineapple','grapes','blueberry','strawberry']
superheroes=['superman','batman','aquaman','sandman','spiderman','wonderwoman','ironman','captain america']
movies=["Inside Out","The princess and the frog","Beauty and the beast","Boss Baby","Cinderella"]
name=input("Enter your name:")
print("Hello",name.capitalize(),"let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess!")
time.sleep(2)
print("Let's begin the game")
time.sleep(1)
userGuesslist = []
userGuesses = []
playgame = True
category = ""
continueGame = "Y"
while True:
    while True:
        if category.upper()=='S':
            secret_word=random.choice(superheroes)
            break
        elif category.upper()=='F':
            secret_word=random.choice(fruits)
        elif category.upper()=='M':
            secret_word=random.choice(movies)
            break
        else:
            category=input("Please select a vaild category:\nF for fruits\nS for superheros\nM for movies\nX to exit\n")
            if category.upper()=='X':
                print("Bye, see you next time!")
                playgame=False
                break
        if playgame:
            secretWordList=list(secret_word)
            attempts=(len(secret_word)+2)
        def printGuessedLetter():
                print("Your Secret word is:"+''.join(userGuesslist))

            #Adding blank lines to userGuesslist to create the blank secret word
        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()
        print("The number of allowed guesses for this word is:", attempts)

            #starting the game
        while True:

            print("Guess a letter:")
            letter = input()
            if letter in userGuesses:
                print("You already guessed this letter, try something else.")
            else:
                attempts -= 1
                userGuesses.append(letter)
            if letter in secretWordList:
                print("Nice guess!")
                if attempts >0:
                    print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

            else:
                print("Oops! Try again.")
                if attempts > 0:
                    print("You have ", attempts, 'guess left!')
                printGuessedLetter()
                    #Win/loss logic for the game
        joinedList = ''.join(userGuesslist)
        if joinedList.upper() == secret_word.upper():
            print("Yay! you won.")
            break
        elif attempts == 0:
            print("Too many Guesses!, Sorry better luck next time.")
            print("The secret word was: "+ secret_word.upper())
            break

        #Play again logic for the game
    continueGame = input("Do you want to play again? Y to continue, any other key to quit")
    if continueGame.upper() == 'Y':
        category = input("Please select a valid categary: F for Fruits / S for Super-Heroes")
        userGuesslist = []
        userGuesses = []
        playGame = True
    else:
        print("Thank You for playing. See you next time!")
        break"""


import random,time
fruits=['pear','mango','apple','banana','apricot','pinapple','grapes','blueberry','strawberry']
superheroes=['superman','batman','aquaman','sandman','spiderman','wonderwoman','ironman','captain america']
movies=["inside out","The princess and the frog","Beauty and the beast"]
name=input("Enter your name:")
print("Hello",name.capitalize(),"let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer")
time.sleep(1)
print("You can guess only one letter at a time.Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let's begin the game")
time.sleep(1)
userGuesslist = []
userGuesses = []
playgame = True
category = ""
continueGame = "Y"
while True:
    while True:
        if category.upper()=='S':
            secret_word=random.choice(superheroes)
            break
        elif category.upper()=='F':
            secret_word=random.choice(fruits)
            break
        elif category.upper()=='M':
            secret_word=random.choice(movies)
            break
        else:
            category=input("Please select a vaild category:\nF for fruits\nS for superheros\nM for movies\nX to exit\n")
            if category.upper()=='X':
                print("Bye.see you next time")
                playgame=False
                break
    if playgame:
        secretWordList=list(secret_word)#apple=5
        attempts=(len(secret_word)+2)
    def printGuessedLetter():
            print("Your Secret word is: " + ''.join(userGuesslist))


        #Adding blank lines to userGuesslist to create the blank secret word
    for n in secretWordList:
        userGuesslist.append('_')
    printGuessedLetter()    
    print("The number of allowed guesses for this word is:", attempts)


        #starting the game
    while True:

        print("Guess a letter:")
        letter = input()
        if letter in userGuesses:
            print("You already guessed this letter, try something else.")
        else:
            attempts -= 1
            userGuesses.append(letter)
            if letter in secretWordList:
                print("Nice guess!")
                if attempts >0:
                    print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

            else:
                print("Oops! Try again.")
                if attempts > 0:
                    print("You have ", attempts, 'guess left!')
                printGuessedLetter()
                    #Win/loss logic for the game
        joinedList = ''.join(userGuesslist)
        if joinedList.upper() == secret_word.upper():
            print("Yay! you won.")
            break
        elif attempts == 0:
            print("Too many Guesses!, Sorry better luck next time.")
            print("The secret word was: "+ secret_word.upper())
            break

        #Play again logic for the game
    continueGame = input("Do you want to play again? Y to continue, any other key to quit")
    if continueGame.upper() == 'Y':
        category = input("Please select a valid categary: F for Fruits / S for Super-Heroes")
        userGuesslist = []
        userGuesses = []
        playGame = True
    else:
        print("Thank You for playing. See you next time!")
        break


                
                      
        
        
   
