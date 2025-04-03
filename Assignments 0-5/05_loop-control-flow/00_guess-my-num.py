import random
def main():
    number_to_guess = random.randint(0, 99)
    guess = -1

    while guess != number_to_guess:
        guess = int(input("Enter a guess: "))
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
    
    print(f"Congrats! The number was: {number_to_guess}")

if __name__ == "__main__":
    main()
