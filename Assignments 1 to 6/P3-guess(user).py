import random 
def guess(x):
    low =1
    high=x
    ans=''
    while ans != 'c':
        if low!= high:
            guess = random.randint(low, high)
        else: 
            guess = low
        ans= input(f'Is {guess} too high (H), too low (L), or is it correct (C)? ').lower()
        if ans == 'h':
            high = guess-1
        elif ans == 'l':
            low = guess+1
    print(f'Wohoo, Computer guessed the number, {guess} correctly!')    
guess(10)
