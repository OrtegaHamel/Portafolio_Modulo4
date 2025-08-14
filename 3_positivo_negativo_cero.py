# Decide si un número es positivo, negativo o cero

print("\n--- Número positivo, negativo o cero ---")

num = float(input("Inserta un número: "))

if num > 0:
    print(f"El número {num} es positivo")
elif num < 0:
    print(f"El número {num} es negativo")
else:
    print("El número es cero")