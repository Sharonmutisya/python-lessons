# return(getting answer back)
# A function prints things,but it canalso give value back with return.
def add(a, b):
    result = a+b
    return(result)
answer = add(5, 3)
print("5+3 =", answer)
print("10+20 =", add(10, 20))

# Functions with decisions and loops.
def song_length(minutes):
    if minutes < 2:
        return "Short"
    elif minutes > 3:
        return "Regular"
    else:
        return "Long"
    print(song_length(10))
    print(song_length(3))
    print(song_length(8))
    print(song_length(1))