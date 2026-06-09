def solicitar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def formatear(resultado):
    if resultado.is_integer():
        return int(resultado)
    return resultado

def calcular(num1, num2, opcion):
    if opcion == 1:
        return formatear(num1 + num2)
    elif opcion == 2:
        return formatear(num1 - num2)
    elif opcion == 3:
        if num2 == 0:
            return "Error: No se puede dividir entre cero."
        return formatear(num1 / num2)
    elif opcion == 4:
        return formatear(num1 * num2)

def main():
    print("-- Calculadora --")

    num1 = solicitar_numero("Ingrese un número: ")
    num2 = solicitar_numero("Ingrese el otro número: ")

    while True:
        print("\nMenú de opciones")
        print("1. Sumar")
        print("2. Restar")
        print("3. Dividir")
        print("4. Multiplicar")
        print("5. Salir")

        try:
            opc = int(input("Ingrese una opción: "))

            if opc == 5:
                print("Hasta luego.")
                break

            if 1 <= opc <= 4:
                resultado = calcular(num1, num2, opc)
                print("Resultado:", resultado)
            else:
                print("Opción no válida.")
        except ValueError:
            print("Error: Ingrese un número entero para la opción.")

if __name__ == "__main__":
    main()