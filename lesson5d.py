# Adding up with a loop,variable that collects a total.
total = 0
for number in range(1, 6):
    total = total + number
    print(f"Add {number}, total now is {total}")
    print("Final total:", total)