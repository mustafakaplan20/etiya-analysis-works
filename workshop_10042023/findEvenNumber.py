def findEvenNumber(upperLimit:int):
  for i in range(0,maxLimit):
    if i % 2 == 0:
      print(i, end=" ")
  

maxLimit = int(input("Üst limit giriniz:"))
findEvenNumber(maxLimit)

print("\n")

def developedEvenNumber(lowerLimit: int, upperLimit:int):
  for i in range(lowerLimit,upperLimit):
    if i % 2 == 0:
      print(i, end=" ")

altLimit = int(input("Bir alt limit giriniz :"))
maxLimit = int(input("üst limit giriniz :"))

developedEvenNumber(altLimit,maxLimit)


    