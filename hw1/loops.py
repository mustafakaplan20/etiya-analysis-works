credits = ["Mortgage Loan", "Personal Loan", "Auto Loan"]

# It gets each element in list
# Alias
for x in credits:
    print("<option>"+x+"<option>")

# Same as above
for x in range(len(credits)):
    print(credits[x])

# It gets the number from 3(included) to 10(not included)
for x in range(3,10):
    print(x)

# It gets the number from 0(included) to 11(not included) increment by 2
for x in range(0,11,2):
    print(x)