

# x= int(input("Enter first number: "))
# y= int(input("Enter second number: "))

# def diff(x,y):
#     return x-y


# result = diff(x, y)
# print(f"The result of the difference is: {result}")


import random

def random_number():
    random_num = random.randint(1, 100)
    user_guess = None

    while user_guess != random_num:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess == random_num:
            print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, the correct number was {random_num}.")

random_number()