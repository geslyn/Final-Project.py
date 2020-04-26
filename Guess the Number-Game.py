import random
import os

name = input('Hello! What is your name? \n')

randomnumber = random.randint(1, 50)

guess = int (input("Welcome, %s!, Do you want play a game? :) Please guess a number between 1 and 50: " % (name)))

while randomnumber != guess:

 if guess < randomnumber:
     print ("Hint: Your guess is too low! Let's try again.")
     guess = int(input("Guess a number between 1 and 50: "))
    
 elif guess > randomnumber:
     print ("Hint: Your guess is too high! Let's try again.")
     guess = int(input("Guess a number between 1 and 50: "))

print('You guessed it %s! Great job' % (name))
os.system("pause")
