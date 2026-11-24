# Alist is one variable that holdsmany items i.e shopping list.
friends = ["Phoebe", "Joey", "Rachael", "Chandler", "Monica", "Ross"]
print(friends)
print("number of friends:", len(friends))
# Getting one time(index)
# Every item has a position number called an index.
# Counting starts at 0, just like range.
print(friends[1])
print(friends[3])
print(friends[-1])
print(friends[5])
# Changing an item
friends[1] = "Rachael"
print(friends)