import random
max_num = 100
secret_num = random.randint(1, max_num)
print("I'm thinking of a number between 1 and " + str(max_num) + "...")

max_guesses = 3
guesses_left = max_guesses

while guesses_left:
  print("Guesses remaining: " + str(guesses_left))
  guess = int(input("Enter your guess: "))
  if guess == secret_num:
    print("That's correct!")
    break
  elif guess < secret_num:
    print("That's too low.")
  else:
    print("That's too high.")
  guesses_left -= 1
else:
  print("Sorry, you are out of guesses.")

