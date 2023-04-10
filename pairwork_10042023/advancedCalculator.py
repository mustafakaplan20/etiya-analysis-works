def sum(firstNum: float, secondNum: float):
  print(firstNum+secondNum)
def substract(firstNum: float, secondNum: float):
  print(firstNum-secondNum)
def multiplication(firstNum: float, secondNum: float):
  print(firstNum*secondNum)
def divide(firstNum: float, secondNum: float):
  if (secondNum != 0):
    print(firstNum/secondNum)
  else:
    print("Divider cannot be 0, please check!")

def calculator(firstNum:float,secondNum:float,operator:str):
  if operator== "+":
    sum(firstNum=firstNum,secondNum=secondNum)
  elif operator == "-":
    substract(firstNum=firstNum, secondNum=secondNum)
  elif operator == "*":
    multiplication(firstNum=firstNum, secondNum=secondNum)
  elif operator == "/":
    divide(firstNum=firstNum,secondNum=secondNum)
  else:
    print("Please choose a valid operator!")

while True:
  print("--------------------------------------------------\n")
  firstNum= float(input("Enter your 1st number: "))
  operator = input("Choose your operation as ( +,-,*, /) :")
  secondNum= float(input("Enter your 2nd number: "))
  calculator(firstNum=firstNum,secondNum=secondNum,operator=operator)
  isContinue=input("Do you want to continue?(y/n)")
  if(isContinue!="y"):
    print("\nOperation terminated!")
    break
  else:
    pass


