num1 = int(input("digita un numero: "))
num2 = int(input("digita el otro4 numero: "))

if num1 < num2:

    for x in range(num1, (num2 + 1)):

        if x%2 == 0:
            print(f"{x} es par")
        else:
            print(f"{x} es impar")

else:
    print("El numero 1 tiene que  ser mayor al 2")