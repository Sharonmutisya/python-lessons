# What did you work on today?(using input). Append the answer to (diary.txt)with new line at the end.
# then..read..the whole file & print each entry number, like 1.
work = input("What did you work on today?")
with open ("diary.txt", "a", encoding="utf-8") as file:
    file.write(work + "\n")
print("Worked on Write, read, append and missing files in python:")
count = 0
with open("diary.txt", "r", encoding="utf-8") as file:
    for line in file:
        count = count + 1
        print(f"{count}. {line.strip()}")
print(f"You have {count} entries so far")