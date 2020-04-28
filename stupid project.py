import random


print("Winning rules of the rock, paper, scissors: paper beats rock, rock beats scissors, and scissors beats paper")

while True:
    print("Enter choice \n 1. for Rock \n 2. for Paper \n 3. for Scissors")
    
    choice = int(input("Players turn: "))
    
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
        
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
        
    print("user choice is: " + choice_name)
    print("\nNow its the computers turn...")
    
    comp_choice = random.randint(1,3)
    
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
        
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
        
    print("Computer choice is: " + comp_choice_name)
    print(choice_name + " VS" + comp_choice_name)
    
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice == 1)):
        print("paper wins => ", end = "")
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or
      (choice == 3 and comp_choice == 1)):
        print("Rock wins => ", end = "")
        result = "Rock"
    else:
        print("Scissor wins => ", end = "")
        result = "Scissor"
        
    if result == choice_name:
        print("PLAYER WINS!!")
    else:
        print("COMPUTER WINS!!")
    
    print("Do you want to play again? Y/N")
    
    if ans == 'n' or ans == 'N':
        break
        
print("\nThanks for playing Rock Paper Scissors!!")
