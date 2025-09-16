import random

print("🎮 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 20...")

# Generate a random number
secret_number = random.randint(1, 20)

# Let the player guess up to 6 times
for attempts in range(1, 7):
    guess = int(input(f"Attempt {attempts}: Take a guess → "))

    if guess < secret_number:
        print("Too low! 📉")
    elif guess > secret_number:
        print("Too high! 📈")
    else:
        print(f"🎉 Nice! You guessed it in {attempts} tries.")
        break
else:
    print(f"😢 Sorry, the number was {secret_number}. Better luck next time!")
