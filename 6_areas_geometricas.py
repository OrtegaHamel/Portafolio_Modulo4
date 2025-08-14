# Calcula el área de figuras geométricas usando funciones

import math

# Área rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Área círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Área triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# Mostrar menú
def mostrar_menu():
    print("\n--- Calculadora de áreas ---")
    print("1. Rectángulo")
    print("2. Círculo")
    print("3. Triángulo")


while True:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))      
    if opcion == 1:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("El área del rectángulo es:", area_rectangulo(b, h))
    elif opcion == 2:
        r = float(input("Radio: "))
        print("El área del círculo es:", area_circulo(r))
    elif opcion == 3:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("El área del triángulo es:", area_triangulo(b, h))
    else:
        print("Opción no válida")