
PROMPT = "What do you want? "
JOKE = "Why did the programmer quit his job? Because he didn't get arrays (a raise)!"
SORRY = "Sorry I only tell jokes."

def main():
 
    user_input = input(PROMPT).strip().lower()  
    

    if user_input == "joke":
    
        print(JOKE)  
    else:
        print(SORRY)  

if __name__ == "__main__":
    main()