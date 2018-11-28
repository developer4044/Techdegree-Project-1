import random


# Change the secret number 'the_number'
def get_new_secret_number():
    return random.randint(1, 100)


# The secret number
the_number = get_new_secret_number()
number_found = False
user_tries = 0

print("I have a number in my mind, can you guess what is the number?")
print("Challenge accepted! Pick a number between 1 and 100")




# Give the player some hint!
def print_hint(user_number):
    if user_number > the_number:
        print("Try lower")

    if user_number < the_number:
        print("Try higher")


while not number_found:
    user_answer = -1
    try:
        user_input = input("Guess a number: ")
        user_answer = int(user_input)
        if user_answer != the_number:
            print_hint(user_answer)
            user_tries += 1

        else:
            print("{} is the number. You found it. after {} tries.".format(the_number, user_tries))
            play_again = input("Play again? Y/N ")
            if play_again.upper() == 'Y':
                the_number = get_new_secret_number()
                continue
            else:
                print("Good Bye!")
                break

    except ValueError:
        print("Oh,Not that way :D, try again")
        continue
