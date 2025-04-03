def double_elements(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

def main():
    numbers = [1, 2, 3, 4]
    doubled_numbers = double_elements(numbers)
    print("The doubled numbers are:", doubled_numbers)

if __name__ == '__main__':
    main()
    
