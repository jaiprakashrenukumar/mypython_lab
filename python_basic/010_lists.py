it = ["jai", "john", "ram", "kiran", "dinesh"]
print(it[1])
print(it[4])

print("\n")
print("it name list: ")
print(it)
print("\n")

# adding a name at the last in the list
print("adding a name in the list")
it.append("karthik")
print(it)
print("\n")

# adding a name to any position in a list here will add sathish at first and mani after ram
print("adding a sathish first in the list and mani next to ram")
it.insert(0, "sathish")
print(it)
print("\n")
it.insert(4, "mani")
print(it)
print("\n")

# remove jai from the list
print("remove jai from the list")
it.remove("jai")
print(it)
print("\n")

# reverse the list
print("reverse the list")
it.reverse()
print(it)
print("\n")

numbers = [5, 3, 8, 1, 0, 9, 12]

# sorting the list
print("sorting the list")
it.sort()
print(it)
print("\n")
numbers.sort()
print(numbers)
