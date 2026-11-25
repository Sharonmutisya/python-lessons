# A dictionary stores items by label, a list stores by position(1, 2, 3).
# Just like a real dictionary, you look up fora word & find it's meaning.
character = {
    "name": "Mariah the scientist",
    "age": 32,
    "career": "singer",
    "proffession": "songwriter"
}
print(character)
print(character["name"])
print(character["career"])

# Using values in sentences.
print(f"{character['name']} is a {character['career']} and {character['proffession']} of {character['age']} yeras old.")

# Changing and adding.
character["age"] = 28
character["status"] = "single"
print(character)

# Removing.
del character["age"]
print(character)

# Missing keys.
print(character.get("genre", "R&B"))

# Checking if key exist.
if "born" in character:
    print("born:", character["georgia"])
else:
    print("atlanta")