def calculator(firstNum:float,secondNum:float,operator:str):
  if operator== "+":
    print(firstNum+secondNum)
  elif operator == "-":
    print(firstNum-secondNum)
  elif operator == "*":
    print(firstNum*secondNum)
  elif operator == "/":
    print(firstNum/secondNum)
  else:
    print("Uygun işlemi seçmediniz!. Lütfen uygun işlemlerden birini seçiniz.")


firstNum= float(input("1.sayıyı giriniz: "))
operator = input("Yapmak istediğiniz işlemi seçiniz ( +,-,*, /) :")
secondNum= float(input("2.sayıyı giriniz: "))
calculator(firstNum=firstNum,secondNum=secondNum,operator=operator)
  
