
#These are the blanks the player has to fill in
blanks  = ["1", "2", "3", "4"]

#The 3 different levels the player has to choose from
quiz_levels = ["easy", "medium", "hard"]

#Number of attempts the user gets to answer correctly per level
attempts = [5,3,1]

#This is the easy version of the quiz, this section of the quiz was taken from the project materials,
#given at the start of the project in the file named: fill-in-the-blanks.py
easy = '''
    A 1 is created with the def keyword. You specify the inputs a 1 takes by
    adding 2 separated by commas between the parentheses. 1 s by default return 3 if you
    don't specify the value to return. 2 can be standard data types such as string, number, dictionary,
    tuple, and 4 or can be more complicated such as objects and lambda functions.
    '''

#This is the medium version of the quiz
medium = '''
    A group of values surrounded by square brackets is a 1. You can add values to a 1 by
    using the 2 method. You can also 3 the 1 if you take a 4 by using the following format 1[x:y]
    '''

#This is the hard version of the quiz
hard = '''
    A type of 1 is created by using a for. You have to end the top line of a 1 with a 2.
    You can stop a 1 by adding a 3. You can move onto the next function if you add a 4.
    '''
#The following variables are meant to be the answers to the different quiz levels
easy_answers = ["function", "values", "none","lists"]
medium_answers = ["list", "append", "index", "slice"]
hard_answers = ["loop", ":", "break", "continue"]

#The following variables assign a number to each of the quiz level to prevent magic numbers
easy_level = 0
medium_level = 1
hard_level = 2

#This is a welcome note to the player
print "\nReady To Test Your Knowledge?\n"

'''
This function's behavior is to set boundaries for the level
The input for this function is level
The outputs for this function is question_level, answers_level, number_of_attempts, level
'''
def boundaries(level):
    if level == quiz_levels[easy_level]:
        question_level = easy
        answers_level = easy_answers
        number_of_attempts = attempts[easy_level]
        return question_level, answers_level, number_of_attempts, level
    elif level == quiz_levels[medium_level]:
        question_level = medium
        answers_level = medium_answers
        number_of_attempts = attempts[medium_level]
        return question_level, answers_level, number_of_attempts, level
    elif level == quiz_levels[hard_level]:
        question_level = hard
        answers_level = hard_answers
        number_of_attempts = attempts[hard_level]
        return question_level, answers_level, number_of_attempts, level
    else:
        return None
'''
This function's behavior is to let the player choose which level of difficulty they will play,
and will be queued off of the boundaries(level) function, if the player types in an incorrect level choice,
they will be asked to input a different level choice.
There are no inputs for this function.
There are no outputs for this function.
'''
def set_level():
    print "Please choose from the following difficulty levels: " + quiz_levels[easy_level] + ", " + quiz_levels[medium_level] + " and " + quiz_levels[hard_level] + ".\n"
    while True:
        level = raw_input("Your level? ")
        level = level.lower()
        if level in quiz_levels:
            return boundaries(level)
        else:
            print "You did not enter a valid level. Please choose between " + quiz_levels[easy_level] + ", " + quiz_levels[medium_level] + " and " + quiz_levels[hard_level] + "."

#This assigns the following variables to the correct level of the quiz
question_level, answers_level, number_of_attempts, level = set_level()

'''
This function's behavior will let the player know how many attempts they have per line to finish the quiz & the question_level.
The inputs of this function are number_of_attempts, level, question_level.
The outputs of this function are none.
'''
def rules(number_of_attempts, level, question_level):
    print "\nYou will have " + str(number_of_attempts) + " attempts for each blank to finish the quiz."
    print "\nThe " + level + " quiz will start now:"
    return question_level

'''
This function's behavior will determine if the player input was correct & will replace the blank with the correct answer.
The inputs of this function are user_input, question_level, index.
The output of this function is question_level.
'''
def correct_answer(user_input, question_level, index):
    question_level = question_level.replace(blanks[index],user_input)
    return question_level

'''
This function's behavior will alert the player if their input was incorrect & reduces the number of attempts by 1 for an incorrect answer,
And will display the number_of_attempts remaining to the player.
The input of this function is number_of_attempts.
The output of this function is updated number_of_attempts in a message to the player
'''
def incorrect_answer(number_of_attempts):
    number_of_attempts -= 1
    if number_of_attempts == 1:
        print "There is " + str(number_of_attempts) + " attempt left."
    else:
        print "There are " + str(number_of_attempts) + " attempts left."
    return number_of_attempts

'''
This function's behavior will first print the rules of the game,
Then the player will be asked to fill in the blanks,
Once a player types in an answer, it will be validated against the correct_answer & incorrect_answer functions,
If the answer is correct the blank will be replaced with the correct_answer and the player will move onto the next blank,
If the answer is incorrect the player will be told they are inccorect, the number_of_attempts they have left and to try again,
Once the number_of_attempts goes to 0 then the player will be prompted with a message that the quiz is over.
The inputs of this function are question_level, answers_level, number_of_attempts, level.
The outputs of this function are blank with updated blank value, incorrect_answer message with number_of_attempts left.
'''
def quiz(question_level, answers_level, number_of_attempts, level):
    index = 0
    print rules(number_of_attempts, level, question_level)
    while index < len(blanks) and number_of_attempts > 0:
        user_input = raw_input("\nPlease fill in an answer for " + blanks[index] + ": ")
        if user_input == answers_level[index]:
            print "\nCorrect!\n"
            question_level = correct_answer(user_input, question_level, index)
            print question_level
            index += 1
        else:
            print "Incorrect."
            number_of_attempts = incorrect_answer(number_of_attempts)
    if number_of_attempts == 0:
        return "\nQuiz OVER! You used all your tries."
    else:
        return "\nCONGRATULATIONS! You answered all the blanks correctly."

print quiz(question_level, answers_level, number_of_attempts, level)
