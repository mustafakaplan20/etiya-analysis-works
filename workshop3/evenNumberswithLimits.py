altLimit = int(input("Bir alt limit giriniz :"))
maxLimit = int(input("üst limit giriniz :"))
for i in range(altLimit,maxLimit):
  if i % 2 == 0:
    print(i, end=" ")