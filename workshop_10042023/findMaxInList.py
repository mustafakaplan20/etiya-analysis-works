def findMaxInList(liste: list):
  print(max(liste))

myList=[]
for x in range(10):
  sayi=float(input("Lütfen sayı giriniz: "))
  myList.append(sayi)

findMaxInList(liste=myList)