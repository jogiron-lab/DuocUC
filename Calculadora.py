print("-- Calculadora --")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese el otro numero: "))

while True:
    print("Menu de opciones\n1. Sumar\n2. Restar\n3. Dividir\n4. Multiplicar")
    opc = int(input("Ingrese una opcion: "))

    if opc == 1:
        print("La suma es:", num1 + num2)
        break
    elif opc == 2:
        print("La resta es:", num1 - num2)
        break
    elif opc == 3:
        print("La division es:", num1 / num2)
        break
    elif opc == 4:
        print("La multiplicacion es:", num1 * num2)
        break