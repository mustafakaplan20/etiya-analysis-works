num=int(input("Write a number!"))

total=0
for i in range(1,num):
  if(num % i==0):
    total+=i

if(total==num):
  print(f"{num}->Perfect Number")
else:
  print(f"{num}->Not perfect number!")