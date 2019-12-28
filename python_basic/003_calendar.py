import calendar

print("\n")
# prints week header ex. Mon Tue  for Mo Tu specify 2 in arugment
print("Below are Weekheaders lists:")
print(calendar.weekheader(3))
print("\n")

#first weekday is monday as per the python hence value is 0
print("value of first week day is :")
print(calendar.firstweekday())
print("\n")

# python start the first weekday by monday and the vaule is 0 hence below output will be 2 since it is wednesday
print("the week day value of 25-12-2019 is:")
print(calendar.weekday(2019, 12, 25))
print("\n")


# month table
print("december 2019 month table:")
print(calendar.month(2019, 12))
print("\n")

# Month in matrix format 


print("december 2019 month table in matrix format:")
print(calendar.monthcalendar(2019, 12))
print("\n")

#in above output week header will be 2 characters use w=3 to change the header
print("december 2019 month table with weekheaders 3 strings: ")
print(calendar.month(2019, 12, w=3))
print("\n")

# complete year
print("calendar of 2020:")
print(calendar.calendar(2020))
print("\n")

#given year is a leap year true and false
print("Is 2019 is leap year True or False ?: ")
is_leap = calendar.isleap(2019)
print(is_leap)
print("\n")


print("Is 2024 is leap year True or False ?: ")
is_leap = calendar.isleap(2024)
print(is_leap)
print("\n")

# find how many leapyear in a given range note: it will not take last year specified
print("how many leap year present in the range 2000-2021: ")
leapyear_count = calendar.leapdays(2000, 2021)
print(leapyear_count)
print("\n")


