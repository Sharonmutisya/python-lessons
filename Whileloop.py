# The while loop
# for loop repeats a set number of times.
# while loop repeats as long as something is true.
age = 28
while age > 20:
    print(f"Getting old now, turning: {age}")
    age = age -1
    print("old")
    # loop until the user gets it right.
    # while is great with input()
    secret = "Love"
    guess = ""
    while guess != secret:
        guess = input("Guess the secret word:")
        print("Gotit")