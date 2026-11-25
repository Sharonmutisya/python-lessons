#Loops tells Python to repeat lines instead of writing the same line many times
for number in range (5):
    print("I am hungry", number)
    print("Need to take some breakfast")
    for number in range (0, 9):
        print(number)
        for number in range (1, 15, 4):
            print(number)
            # Countdown
            for count in range (5, 0, -1):
                print(f"T -minus {count}...")

# A list of dictionaries.
# Is thecommon real world pattern.
characters = [
    {"name": "Rihanna", "babies": 3, "nickname": "Badgalriri"},
    {"name": "Cardi-B", "babies": 4, "nickname": "Bacardi"},
    {"name": "NickiMinaj", "babies": 1, "nickname": "Barbie"}
]
for character in characters:
    print(f"{character['name']} has {character['babies']} babies, she's also called {character['nickname']}")
    print("First character:", characters[0]["name"])