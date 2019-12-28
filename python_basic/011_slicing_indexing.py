digits = [0,1,2,3,4,5,6,7,8,9]
print(digits)
print("\n")

# 5 character in the list
print("5 character in the list")
print(digits[5])
print("\n")

####################################################################
#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array

##################################################################3

print("display all the digits")
print(digits[0:9]) # it excludes the 9th value and it prints rest
print("\n")

print("display till 3" )
print(digits[:4])
print("\n")

print("display last digit" )
print(digits[-1])
print("\n")

print("display last two digits" )
print(digits[-2:])
print("\n")

print("display last 5 digits" )
print(digits[-5:])
print("\n")

print("display all digits" )
print(digits[::])
print("\n")

print(digits[::2])
print("\n")

print(digits[::3])
print("\n")

print(digits[::-2])
print("\n")

print(digits[::-3])
print("\n")
