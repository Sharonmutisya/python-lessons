# Looping over list
# List hold several valuesin one variable, inside square brackets[],separated by commas.
vegetables = ["Cabbage", "Spinach", "Brocolli", "lettuce"]
for foods in vegetables:
    print("I'm a vegetarian, I love", vegetables)
    # Loop + if together
    for number in range(2, 10):
        if number % 5 == 0:
            print(number, "is odd")
        else:
            print(number, "is even")
#Looping through list
friends = ["Rachael", "Joey", "Marcus", "Sharon"]
for characters in friends:
    print(f"Meet {friends}!")
    for index, character in enumerate(characters):
        print(f"Number {index + 1}: {friends}")