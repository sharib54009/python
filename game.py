import random

# Computer chooses a random number
secret_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low 📉 Try again!")
    elif guess > secret_number:
        print("Too high 📈 Try again!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
