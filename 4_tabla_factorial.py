# Muestra la tabla de multiplicar o calcula el factorial de un número

print("\n--- Tabla de multiplicar o factorial ---")
print("1. Tabla de multiplicar")
print("2. Factorial")
opcion = int(input("Elige una opción: "))

if opcion == 1:
    n = int(input("¿Tabla del...? "))
    print(f"\nTabla del {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
elif opcion == 2:
    n = int(input("Número para factorial: "))
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"{n}! = {factorial}")
else:
    print("Opción inválida")