# Looping through a dictionary.
character = {"name": "Mariah", "career": "Music", "proffession": "Songwriter"}
print(type(character))
for key in character:
    print(key)
    for key, value in character.items():
        print(f"{key} -> {value}")