# With files your program can save information & load it back the next time it runs.
# ...open("...") is a function  thatopens a file.
# (movies.txt) It's the file name.Python creates it ifit does'nt exist.
# "w" the mode, meaning write
# (encoding="utf-8") tells python how to store characters, makes sure emojis save & load correctly.
# \n special code meaning new line(like pressing enter).Withou it all text would be squashed onto one line.
with open("movies.txt", "w", encoding="utf-8") as file:
    file.write("🎬Expendables is my favorite action\n")
    file.write("🎥Friends is more relatable sitcom\n")
    file.write("🎬Blacklist has thrill moments\n")
    print("File saved")

# Reading a file.."r"is the mode for read.
# file.read..reads the whole file as one piece of text&store it in (content).
with open("movies.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

# Reading line by line.
# line.strip..removes invisible \nat the end of each line,plus extra spaces.
with open("movies.txt", "r", encoding="utf-8") as file:
      for line in file:
            print(line.strip())
# file.readlines()..gives back a list where each item is one line, including \n.
with open("movies.txt", "r", encoding="utf-8") as file:
      lines = file.readlines ()
print(lines)
print("Number of ideas", len(lines))

# Adding to a file(append)
# To add files without erasing, use "a" for append.
with open("movies.txt", "a", encoding="utf-8") as file:
      file.write("💥TBBT it's hard to relate if you're not a nerd\n")
print("Idea added")