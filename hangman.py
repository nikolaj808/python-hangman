import os
import sys
import random

attempts = 0
randomCount = random.randint(0, 854)
randomWord = ""
guess = list()
guessOutput = ""
wrongList = ""
rightCounter = 0
done = False

with open("words.txt") as fp:
	line = fp.readline()
	cnt = 1
	while line:
		line = fp.readline()
		if cnt== randomCount:
			randomWord = line.strip()
			break
		cnt += 1

print("Welcome to Hangman!")
attempts = int(input("How many attempts do you need? "))
print("Then let's get started.")

print(randomWord)
for letters in randomWord:
	guess += "*"
guessOutput = "".join(guess)

while (not done):
	print("You have " + str(attempts) + " attempts left.")
	print(guessOutput + "\n")
	print("Guess a single letter or guess the whole word")
	print("Wrong guesses: " + wrongList)

	guessInput = input()
	
	attempts -= 1
	if attempts < 1:
		done = True
	if len(guessInput) > 1:
		if guessInput == randomWord:
			guessOutput = guessInput
			done = True
		else:
			wrongList += guessInput + ", "
	else:
		counter = 0
		for letters in randomWord:
			if (letters == guessInput):
				guess[counter] = guessInput
				rightCounter += 1
			counter += 1
		if rightCounter == 0:
			wrongList += guessInput + ", "
		guessOutput = "".join(guess)
		if guessOutput == randomWord:
			done = True
		rightCounter = 0

	os.system("clear")

if (guessOutput == randomWord and attempts == 0):
	print("You win! And on your last attempt too!")
elif guessOutput == randomWord:
	print("You win! You had " + str(attempts) + " attempts left")
else:
	print("You lost! Better luck next time")
print("The word was: " + randomWord)