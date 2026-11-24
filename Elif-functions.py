# Functions with decisions and loops.
def song_length(minutes):
    if minutes < 2:
        return("Short")
    elif minutes < 4:
        return("Regular")
    else:
        return("Long")
print(song_length(10))
print(song_length(3))
print(song_length(6))
print(song_length(1))