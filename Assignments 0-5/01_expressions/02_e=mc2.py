def main():
    C = 299792458  
    
    while True:
        mass_input = input("Enter kilos of mass (or 'quit' to exit): ")
        if mass_input.lower() == 'quit':
            print("Exiting the program...")
            break
        
        try:
            mass = float(mass_input)
            energy = mass * C ** 2
            print(f"e = m * C^2...\nm = {mass} kg\nC = {C} m/s\n{energy} joules of energy!")
        
        except ValueError:
            print("Please enter a valid number for mass.")
if __name__ == '__main__':
    main()
