import random
import math

# Taking Inputs
first_num = int(input("Enter the first number:- "))

# Taking Inputs
second_num = int(input("Enter second number:- "))

# generating random number between
# the lower and upper
x = random.randint(first_num, second_num)

##returns natural logrithm of numbers
print("\n\tYou've only ",
      round(math.log(second_num - first_num + 1, 2)),
      " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count <= math.log(second_num - first_num + 1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(second_num - first_num + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time")
