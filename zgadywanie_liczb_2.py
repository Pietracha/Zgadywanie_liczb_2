"""
Program will guess a number imagined by user.
"""
def intro():
    """
    Introduction function
    :return: game invitation line
    """
    print("Choose a number from 0 to 1000 and I will guess it in maximum 10 tries.")


def main_func():
    """
    Main game function
    """
    minimum = 0
    maximum = 1000
    intro()
    i = 0 # computer's tries counter
    while i <= 9: # checking if user s not cheating by limiting the function to 10 loops
        guess = int((maximum - minimum) / 2) + minimum
        print(f"My guess is: {guess}")
        print("Choose 1, 2 or 3:")
        print("(1) Too low\n"
              "(2) Too high\n"
              "(3) You win!\n")
        try: # failsafe for wrong input type
            hint = int(input())
        except ValueError:
            print("Choose 1, 2 or 3!")
            continue
        if hint == 1:
            minimum = guess
            i += 1 # computer's tries counter increased
        elif hint == 2:
            maximum = guess
            i += 1
        elif hint == 3:
            print("I win!")
            break
    else:
        print("You are cheating!") # displayed when counter hits 10


main_func()
