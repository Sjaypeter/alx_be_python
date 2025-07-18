while True:
    size_of_pattern = int(input("Enter the size of the pattern: "))
    symbol = input("Enter your symbol: ")
    for x in range(size_of_pattern):
        for y in range(size_of_pattern):
            print(symbol, end=" ")
        print()

        