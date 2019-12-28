
names = 'jai, suresh, vikram, santhosh'
print(names) # this prints as a long string
print("\n")

# now we are going to split this string

l = names.split(", ") # we are spliting using , and space 
print(l)
print("\n")

print("another example")
newlist = 'jai1suresh1vikram1santhosh'
print(newlist)
print("\n")

nl = newlist.split("1")
print(nl)
print("\n")
############################ now joining a string ######################
print("example for joining the string")
csv = ','.join(nl)
print(csv)
print("\n")

friends = ' and '.join(nl)
print(friends)
