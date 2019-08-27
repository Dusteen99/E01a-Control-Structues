#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen

#The four lines of text above are explained already, except the first one which tells the computer where to find python.


print('Greetings!') #This line prints Greetings!
colors = ['red','orange','yellow','green','blue','violet','purple'] #Creates an array called colors containing strings.
play_again = '' #Assigns an empty string to a variable caleld play_again.
best_count = sys.maxsize            # the biggest number, assigns the highest number the system can handle, which is based on operating system, to best_count.
while (play_again != 'n' and play_again != 'no'): #Creates a while loop where the condition only returns true when play_again is not "n" or "no" exactly.
    match_color = random.choice(colors) #Assigns a random color from the colors array to match_color.
    count = 0 #Sets count to 0.
    color = '' #Sets color to an empty string.  
    while (color != match_color): #Another while loop that has a condition that returns true when the color variable is not the random color.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line, asks user for input that is assigned to color, creating a new line before printing it.
        color = color.lower().strip() #Removes whitespace and lowercases the string.
        count += 1 #Increments count by one.
        if (color == match_color): #If statement that has a condition that returns true when color and match color are exact matches.
            print('Correct!') #Prints Correct! if the colors are the same.
        else: #The else, which is what would be run if the condition from before returned false.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #Prints the number of guesses, which is the count variable.
    print('\nYou guessed it in {0} tries!'.format(count)) #Prints the text with the number of guesses after the while loop is done.
    if (count < best_count): #Tests to see if count is less than the previous best lowest count.
        print('This was your best guess so far!') #Prints the text if the line before returns true.
        best_count = count #Reassigns the new best count to best_count.
    play_again = input("\nWould you like to play again? ").lower().strip() #Asks the user for input on whether they want to play more or not. If they put "n" or "no", it terminates. Otherwise the loop starts again.
print('Thanks for playing!') #Prints this if the user says no to the question before, no longer in the loop so program terminates.