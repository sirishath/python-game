''' This is a fun guessing game in which you are supposed to guess a 4-digit number that is being generated.
If you get femi that means one number is in right position, if u get pico it means right number in wrong position 
and if u get bagels it means wrong number....
Enjoy the gameeee'''
import random
NUM_DIGITS = 4    # number of digits in the number to be guessed

def intro():
    '''
    Introduces the game and explains the clues
    '''
    print('Welcome to Bagels!')
    print()
    print(f"I'm thinking of a {NUM_DIGITS} digit number. Each digit is between")
    print("1 and 9. Try to guess my number.")
    print()
    print("I'll say \"fermi\" for each correct digit in the correct position.")
    print("I'll say \"pico\" for each correct digit in the wrong position.")
    print("I'll say \"bagels\" if all of the digits are wrong.")
  
  
def get_clues(secret_string, guess_string):
    """
    Creates the clues for the user depending on how of the user's guess match
    the secret number to be guessed.
    
    Params:
    secret_string: The number to be guessed as a string
    guess_string: The number guessed by the user as a string
    
    Returns:
    a string of clues
    """
    # create lists to cleverly use to determine the clues
    secret_list = list(secret_string)
    guess_list = list(guess_string)
    clues = ''
    
    # check for any correct digits in the correct position
    for index in range(NUM_DIGITS):
        if guess_list[index] == secret_list[index]:
            clues = clues + 'fermi '
            guess_list[index] = 'X'
            secret_list[index] = 'Y'
    
    # check for any correct digits in the wrong position
    for index in range(NUM_DIGITS):
        for index2 in range(NUM_DIGITS):
            if secret_list[index] == guess_list[index2]:
                clues = clues + 'pico '
                secret_list[index] = 'Y'
                guess_list[index2] = 'X'
   
    # if clues is '' then there were no correct digits
    if clues == '':
        clues = 'bagels'
        
    return clues


def get_secret_number():
    '''
    Randomly generates the number the user will guess stored as a string
    Each digit must be 1-9 inclusive
    
    Returns:
    the secret number as a string of digits each digit 1-9
    '''
    random_num = ''
    for i in range(NUM_DIGITS):
        number_generate = random.randrange(1,9)
        number_generate = str(number_generate) 
        random_num = number_generate + random_num
    #print(random_num)
    random_num = random_num.strip()
    return random_num



        


def is_guess_valid(guess):
    """
    Determines if the guess is valid. To be valid, it must have NUM_DIGIT characters,
    each character must be a digit, and none of the characters can be a '0'.
    
    Param:
    guess (str): the guess made by the user
    Returns:
    True if the guess is valid; False otherwise
    """
    if len(guess) == NUM_DIGITS:
        if guess.isdigit():
            #print("yes it is digit")
            return True
        else:
            #print("no digit")
            return False 
    
    
    else:
        #print("wrong size")
        return False 
   
    


def get_user_guess():
    '''
    This function repeatedly asks the user to make a guess until the guess is valid.
    
    Returns:
    The valid guess entered by the user as a string
    '''
    userInput = input("Your guess? ")
 
    
    while not(is_guess_valid(userInput)):
        print("You must enter 4 digits with no zeros. Try again.")
        userInput = input("Your guess? ")
        print(userInput)
        is_guess_valid(userInput)

        
    #print(userInput)
    return userInput
    


def play_one_round():
    """
    Plays one round from generating the number to be guessed until the user guesses the number.
    When the user guesses the number, the number of guesses it took is displayed.
    """
    secret_number = get_secret_number()
    #print("sec",type(secret_number))
    #print(secret_number)
    guess_number = get_user_guess()
    #print("looppp",guess_number)
    
    count = 0

    
    while (secret_number != guess_number):
        count = count + 1 
        clues = get_clues(secret_number, guess_number)
        print(clues) 
        #guess_number = input("Your guess? ")
        guess_number = get_user_guess()
        #print("loop",guess_number)
    
        
    #print(count)
        
    if secret_number == guess_number:
        count = count + 1 
        print(f"You got it in {count} guesses.")
    
    #print(count) 
    
    
 

def play_again():
    """
    The function asks the user if they want to play again until
    the user answers 'y' or 'n', upper or lower case.
    
    Returns:
    the lowercase version of the user's y/n response lower case
    """

    while True:
        response = input("Do you want to play again (y/n)? ").lower().strip()
        if response == 'n' or response == 'y':
            return response
        else:
            print("You must answer y or n. Try again.")
            
def main():
    intro()  
    response = 'y' 
    while response == 'y':
        print()
        play_one_round()
        print()
        response = play_again()
        #print(response)

main()

            
           
        

    
   
    
    
    
    
    
