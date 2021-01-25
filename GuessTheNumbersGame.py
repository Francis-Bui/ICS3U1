# Guess the number game - DDC
# uses isdigit() function to check user input
# has "shuffle" function to redo the number and get 5 new tries
import random
    
# initialize global variables used in your code here

guessCount = 7	# set number of guesses to 7
#guessNum = 0	# declare integer variable and set it 0 to start
maxNum = 100	# set muximum number to 100
secretNum  = 27	# declare secret number - any number you want
passphrase = "secret" # secret cheat phrase

#====================================================================
# insert code that asks the user to say what they want as the maxNum
# ask the user to pick how many guesses

# add a cheat line to print the secretNum
#====================================================================

# this line picks a random secret number between 0 and 100
maxNum = int(input("What's the maximum range number?"))
secretNum = random.randrange(0, maxNum + 1)

# define a FUNCTION that get called after each guess 
def inputGuess():
    
    # initialize global variables used in your code here
    global guessCount
    global secretNum
    
    # ask for the player's guess and convert it to an interger
    guessNum = input("What's your guess?")
    
    # take away a guess 
    guessCount -= 1
    
    # check IF they WON =============================
    if guessNum.isdigit():
        guessNum = int(guessNum)

        if (guessNum == secretNum):
            print ("Guess was", guessNum)
            print ("Number of remaining guesses is", guessCount)
            print ("YOU WIN!!!")  
        
        # else, check if they're out of guesses =================
        elif (guessCount == 0):
            print ("Guess was", guessNum)
            print ("You're out of guesses.  The number was", secretNum)
            print ("Thanks for playing!") 

        elif (guessCount == 1):
            print ("Guess was", guessNum)
            print("You have one guess left! You can now use the shuffle command and save yourself!")
            inputGuess()
        # else, check and let them them know if they're too high =================
        elif (guessNum > secretNum) and (guessNum <= maxNum):
            print ("Guess was", guessNum)
            print ("Number of remaining guesses is", guessCount)
            print ("Lower!")
            print ()
            # go back up to inputGuess and get a new guess
            inputGuess()
        
        # else, check and let them them know if they're too low =================
        elif (guessNum < secretNum) and (guessNum >= 0):
            print ("Guess was", guessNum)
            print ("Number of remaining guesses is", guessCount)
            print ("Higher!")
            print()
            # go back up to inputGuess and get a new guess
            inputGuess()
            
        else:
            print ("Your guess was out of range... try again.")
            guessCount += 1
            print ()
            inputGuess()

    else:

        # reveal secret number
        if (guessNum == passphrase):
            print(f"The secret number is {secretNum}")
            guessCount +=1
            inputGuess()  

        # shuffle the secret number
        elif (guessNum == "shuffle") and (guessCount <= 1):
            secretNum = random.randrange(0, maxNum + 1)
            print("Shuffling the number, you get 5 more guesses")
            guessCount +=6
            inputGuess()  

# start the "inputGuess" function
inputGuess()  