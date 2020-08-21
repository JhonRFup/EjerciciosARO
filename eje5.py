num1 = int(input("digita el primer valor:"))
num2 = int(input("digita el segundo valor:"))

if num1 < num2:

    for cont in range(num1, (num2 + 1)):
        print(cont)

else:
  print("El número 1 debe ser menor al numero 2")