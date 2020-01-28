from random import randint

number = randint(0, 20)
game_active = True
print("NUMBER GUESSER GAME")
number_tries = 0


prompt = "Guess a number between 1 and 20"

while game_active:

    guess = int(input(prompt))
    if guess == number:
        print("Correct!")
        print(f"it took you {number_tries} tries to guess")
        break

    elif guess < number:
        print("The number is higher than your guess\n\n\n\n")
        number_tries += 1

    elif guess > number:
        number_tries += 1
        print("The number is lower than your guess\n\n\n\n")

