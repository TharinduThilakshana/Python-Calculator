while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)

  if choice == '#':
    print("Done. Terminating")
    break

  num1 = float(input("Enter first number:"))
  num2 = float(input("Enter second number: "))
  
  if choice == "+":
    print(num1, "+", num2, "=", (num1+num2))
    
  elif choice == "-":
    print(num1, "-", num2, "=", (num1-num2))

  elif choice == "*":
    print(num1, "*", num2, "=", (num1*num2))

  elif choice == "/":
    if num2 == 0.0:
        print("Divide by 0 Error")
    else:
        print(num1, "/", num2, "=", (num1/num2))

  elif choice == "^":
    print(num1, "^", num2, "=", (num1^num2))

  elif choice == "%":
    print(num1, "%", num2, "=", (num1%num2))

  else:
        print("invalid")
