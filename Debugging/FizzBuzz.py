for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    #Divisable by both 3 and 5
    print("FizzbBuzz")
  elif number % 3 == 0:
    #Divisable by 3
    print("Fizz")
  elif number % 5 == 0:
    #Divisable by 5
    print("Buzz")
  else:
    print(number)