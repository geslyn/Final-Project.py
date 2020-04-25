import random
import os

name = input('Hello! What is your name? \n')

randomNumber = random.randint(1, 50)

guess = int (input("Welcome, %s!, Do you want play a game? :) Please guess a number between 1 and 50: " % (name)))

while randomNumber != guess:

 if guess < randomNumber:
     print ("Hint: Your guess is too low! Let's try again.")
     guess = int(input("Guess a number between 1 and 50: "))
    
 elif guess > randomNumber:
     print ("Hint: Your guess is too high! Let's try again.")
     guess = int(input("Guess a number between 1 and 50: "))

print('Great Job! You guessed it')
os.system("pause")
