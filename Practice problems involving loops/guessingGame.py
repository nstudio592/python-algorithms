'''This is a guessing game. The program generates a lucky number between 
1 - 100 and has the player try to guess it. '''
import random

lucky_number = random.randint(1, 100)
guess = 0
count = 1

while guess != lucky_number:
	guess = int(input("Enter a number between 1-100: "))
	if(guess == lucky_number):
		print("You guessed correctly! The lucky number is {} and it only took you {} tries to get it!".format(lucky_number, count))
	elif(guess > lucky_number):
		print("Your guess is too high!")
	elif(guess < lucky_number):
		print("Your guess is too low!")
	else:
		print("Sorry, please enter a valid number.")
	count = count + 1

