def checkPerfectNumber(number: int):
  total=0
  for i in range(1,number):
    if(number % i==0):
      total+=i

  if(total==number):
    print(f"{number}->Perfect Number")
  else:
    print(f"{number}->Not perfect number!")

inputNumber=int(input("Write a number for checking 'Perfect Number' or not"))
checkPerfectNumber(inputNumber)