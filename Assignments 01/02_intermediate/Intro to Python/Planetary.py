def main():

    weight_on_earth = float(input("Enter a weight on Earth: "))
    

    planet = input("Enter a planet: ")

    if planet == "Mercury":
        weight_on_planet = weight_on_earth * 0.376
    elif planet == "Venus":
        weight_on_planet = weight_on_earth * 0.889
    elif planet == "Mars":
        weight_on_planet = weight_on_earth * 0.378
    elif planet == "Jupiter":
        weight_on_planet = weight_on_earth * 2.36
    elif planet == "Saturn":
        weight_on_planet = weight_on_earth * 1.081
    elif planet == "Uranus":
        weight_on_planet = weight_on_earth * 0.815
    elif planet == "Neptune":
        weight_on_planet = weight_on_earth * 1.14
    else:
        print("Invalid planet entered!")
        return

    print(f"The equivalent weight on {planet}: {round(weight_on_planet, 2)}")

if __name__ == '__main__':
    main()
