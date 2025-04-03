def main():
    num_counts = {}
    
    while True:
        num = input("Enter a number: ")
        if num == "":
            break
        num = int(num)
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

if __name__ == '__main__':
    main()
