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
# Adding items..(.append) adds item at the end while 
# (.insert) adds item at chosen position
friends = ["Phoebe", "Joey", "Rachael", "Chandler", "Monica", "Ross"]
friends.append("Janice")
friends.insert(6, "Marcus")
print(friends)
# Removing items...(.remove) removes item with its value.
# (.pop()) removes last item & gives it back to store in variable(last).pop(0)
friends.remove("Marcus")
print(friends)
last = friends.pop()
print("I removed:", last)
print(friends)
# Checking if something in the list.
if "Joey" in friends:
    print("Joey is a friend.")
else:
    print("Joey is not a friends.")