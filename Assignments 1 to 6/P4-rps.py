import random 

def play():
    user = input("Enter 'r' for Rock, 'p' for Paper, and 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It's a tie, try again!")
    elif user == ('r' and computer == 's') or (user == 'p' and computer== 'r') or (user =='s' and computer=='p'):
        print("You Won!")
    else:
        print("Computer Won!")        
print(play())