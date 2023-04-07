number_1 = input("Please write 1st number")
number_1 = float(number_1)

number_2 = input("Please write 2nd number")
number_2 = float(number_2)
result = 0

print("Operation perform as order 1st number and 2nd number!")

operation = input(
    "What kind mathematical operation do you want? '+','-','/','*' ")

if (operation == "+"):
    result = number_1+number_2

elif (operation == "-"):
    result = number_1-number_2

elif (operation == "*"):
    result = number_1*number_2

elif (operation == "/"):
    if (number_2 != 0):
        result = number_1/number_2

    else:
      print("Divider cannot be 0, please check!")

else:
    print("Please choose a valid operator!")

print(result)
