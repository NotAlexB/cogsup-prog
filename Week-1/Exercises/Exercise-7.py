"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

"""Simple game where you choose a number between 1 and 100, which the computer must guess."""

def check_int(s):
    """ Check if string 's' represents an integer. """
    # Convert s to string
    s = str(s) 
    
    if len(s) == 0:
        return False

    # If first character of the string s is - or +, ignore it when checking
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    
    # Otherwise, check the entire string
    return s.isdigit()

def input_integer(prompt):
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    guess = input(prompt) # Ask the user for their guess
    while (not check_int(guess)) or not (int(guess) == 1 or int(guess) == 0 or int(guess) == 2): # Repeat until the user inputs a valid integer
        print('\nYour answer must be either a 0, 1, or 2\n')
        guess = input(prompt)
    return int(guess)

target = 50

print("Pick an number between 1 and 100. And I'll try to find it!\n")
# get user simplified user input
guess = input_integer('Is your number {}?\nPlease, enter a higher(1), lower(0), or correct (2): '.format(target))

# upper and lower bounds of binary search
low = 0
high = 100

while guess != 2: # Repeat until the player says you are correct.
    # binary search for their guess
    if guess == 1:
        low =  low + (high - low) // 2 
    else:
        high =  high - (high - low) // 2
    
    target = (low + high) // 2
        
    guess = input_integer('Is your number {}?\nPlease, enter a higher(1), lower(0), or correct (2): '.format(target))

print("I win! The number was " + str(target))