def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    lst[index] = new_value
    return lst

def slice_list(lst, start, end):
    return lst[start:end]

def main():
    # Initial list to work with
    game_list = ['apple', 'banana', 'cherry', 7, 12]
    
    while True:
        print("\nCurrent List:", game_list)
        print("Select an operation:")
        print("1. Access Element")
        print("2. Modify Element")
        print("3. Slice List")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(game_list, index)
            print("Accessed element:", result)
            
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(game_list, index, new_value)
            print("Modified list:", result)
            
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(game_list, start, end)
            print("Sliced list:", result)
        
        elif choice == '4':
            print("Exiting the game...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
