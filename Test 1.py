import random
import emoji

randomNumber = random.randint(1, 50)

guess = int (input("enter a number between 1 and 50: "))

while randomNumber != guess:

 if guess < randomNumber:
     print ("Hint: Guess is too low! Try again.")
     guess = int(input("enter a number between 1 and 50: "))
    
 elif guess > randomNumber:
     print ("Hint: Guess is too high! Try again.")
     guess = int(input("enter a number between 1 and 50: "))

    
print(emoji.emojize('Great Job! You guessed it :thumbs_up_sign:'))
