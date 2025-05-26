import random 

print("hi welcome to the number guessing game. \n " \
"You have 7 chances to guess the number. Let's start!")

low = int(input("enter the lower bound:"))
high = int(input("enter the upper bound:"))

print(f"\n you have 7 chances to guess the number between {low} and {high}. let's start!")

num = random.randint(low,high)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter+= 1
    guess = int(input('enter your number:'))

    if guess == num:
        print(f'correct! the number is {num}. you guessed it in {guess_counter} attempts.')
        break
    elif guess_counter >= chances and guess != num:
        print(f'orry! the number was {num}. better luck next time.')
    elif guess > num:
        print('too high! try a lower number.')
    elif guess < num:
        print('too low! try a higher number')