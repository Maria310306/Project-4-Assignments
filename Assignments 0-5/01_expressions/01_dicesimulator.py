import random

def main():
    for roll in range(1, 4):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Roll {roll}: Die 1 = {die1}, Die 2 = {die2}")
if __name__ == '__main__':
    main()


