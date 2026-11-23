# Making decision (if and else)
# The age of consent is 18 years
age = int(input("How old are you?"))
if age >= 18:
    print("You can watch adult content")
else:
    print("You can watch kids cartoon")
    print("Enjoying the show")
    # elif- means else if, it adds extra questions.
    age = int(input("How old are you?"))
    if age < 5:
        print("Kids TVshows")
    elif age < 13:
        print("Cartoons")
    elif age < 18:
        print("teens TV shows")
    else:
        print("Adult TV shows")