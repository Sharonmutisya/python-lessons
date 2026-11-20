#Loops tells Python to repeat lines instead of writing the same line many times
for number in range (5):
    print("I am hungry", number)
    print("Need to take some breakfast")
    for number in range (0, 9):
        print(number)
        for number in range (1, 15, 4):
            print(number)
        