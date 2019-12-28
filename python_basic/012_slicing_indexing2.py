digits = [0,1,2,3,4,5,6,7,8,9]


for i in range(len(digits)):
  print(digits[:i])
print("\n")

for i in range(len(digits)):
    print(digits[i:i+3])
print("\n")


windows_size = 3
for i in range(len(digits)-(windows_size-1)):
    print(digits[i:i+windows_size])
print("\n")

