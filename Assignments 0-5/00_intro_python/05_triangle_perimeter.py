def main():
    s1: float = float(input("What is the length of side 1? "))
    s2: float = float(input("What is the length of side 2? "))
    s3: float = float(input("What is the length of side 3? "))

    print("The perimeter of the triangle is " + str(s1 + s2 + s3))
if __name__ == '__main__':
    main()