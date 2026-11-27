# Saving what user types.
# idea=input(...)asks the user, & stores the answer in text.
# enumerate(file, 1)numbers the lines starting from 1 instead of 0.
# if yourun it afew times, each run remembers the idea from earlier run, cause they stored in file not program.
idea = input("Ozark is overrated:")
with open("movies.txt", "a", encoding="utf-8") as file:
    file.write(idea + "\n")
print("All ideas saved:")
with open("movies.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, 1):
        print(f"{number}. {line.strip()}")

# When file doesn't exist.
with open("missing.txt", "r", encoding="utf-8") as file:
    print(file.read())
# "FileNotFounfError:" because such file(missing.txt)is notfound.
# Reading file that isn't there crashes the program.