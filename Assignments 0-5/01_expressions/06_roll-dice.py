import random

def main():
    for roll in range(1, 4):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum_of_dice = die1 + die2
        print(f"Roll {roll}: Die 1 = {die1}, Die 2 = {die2}, Sum = {sum_of_dice}")
if __name__ == '__main__':
    main()