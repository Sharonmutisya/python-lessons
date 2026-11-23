# Adding up with a loop,variable that collects a total.
total = 0
for number in range(1, 6):
    total = total + number
    print(f"Add {number}, total now is {total}")
    print("Final total:", total)
    # Assignment
    for frame in range(1, 6):
        print(f"Rendering frames {frame} of 5")
        if frame == 5:
            print("Last frame")
            print("Video ready")