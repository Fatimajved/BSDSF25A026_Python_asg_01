secret = 37
name = input("Player's naam: ")

attempts = 0
guessed = False

while attempts < 7:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("Invalid! Please enter a number between 1 and 100.")
        continue

    attempts = attempts + 1

    if guess == secret:
        guessed = True
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")

if guessed:
    print("Congratulations", name, "! You guessed it in", attempts, "attempts.")
else:
    print("Sorry", name, "! The secret number was:", secret)