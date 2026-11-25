# Create a dictionary project with the keys [title], [episodes], [minutes].
# Print the sentence using f string. Add new key[platform],
# Loop through with [.items()] and print every [key -> value].
projects = [
    {"title": "Friends", "episodes": 24, "minutes": 20},
    {"title": "Blacklist", "episodes": 22, "minutes": 45},
    {"title": "Lupin", "episodes": 6, "minutes": 52}
]
print(f"{projects['title']} has {projects['episodes']} episodes ands plays for approximately {projects['minutes']} minutes")
