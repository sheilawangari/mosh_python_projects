# While loops are used to execute a block of code multiple times
# Useful in building interactive programs and games
# while condition: As long as the condition is true, the code will be repetitively executed
# While loops also have else statements

secret_number = 9   # Variable to store secret number
guess_count = 0     # The number of guesses the user has made
guess_limit = 3

while guess_count < guess_limit:   # A while loop to repetitively ask a user to take a guess
    guess = int(input('Guess: '))
    guess_count += 1        # Increments by 1

    if guess == secret_number:
        print('You Won!')
        break      # This is used to terminate a loop, jump out of the while loop, it wont ask for another Guess:

else:
    print('Sorry you failed!')   # This is executed when the user makes 3 wrong guesses, the interpreter jumps to this code