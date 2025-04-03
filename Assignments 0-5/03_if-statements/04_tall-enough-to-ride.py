def tall_enough():
    minimum_height = 50
    
    while True:
        height_input = input("How tall are you?(inches) ")

        if height_input == "":
            print("Goodbye!")
            break
        try:
            height = float(height_input)
            if height >= minimum_height:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        
        except ValueError:
            print("Please enter a valid number for height.")

if __name__ == "__main__":
    tall_enough()
