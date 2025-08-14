play_game = input("Do you want to play?(y/n): ").lower()
while play_game =="y":
    size_of_pattern = int(input("Enter the size of the pattern: "))
    for x in range(size_of_pattern):
        for y in range(size_of_pattern):
            print("*", end=" ")
        print()
        play_game = input("Do you want to play?(y/n): ").lower()
    else:
        break

        