def findFibonacci(numberOfterms: int):
  first_element=1
  second_element=1

  fibonacci_list=[]

  if(numberOfterms<0):
    print("Please write valid number, greater & equal to 0!")

  elif(numberOfterms==0):
    fibonacci_list.append(0)
  else:
    fibonacci_list.append(first_element)
    fibonacci_list.append(second_element)
    for i in range(2,numberOfterms):
        third_element=first_element+second_element
        fibonacci_list.append(third_element)
        first_element=second_element
        second_element=third_element

  return fibonacci_list

fibonacciTerms=int(input("How many numbers do you write for Fibonacci?"))
print(findFibonacci(fibonacciTerms))