def in_range(n, low, high):
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the low value: "))
    high = int(input("Enter the high value: "))
    
    if in_range(n, low, high):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()
