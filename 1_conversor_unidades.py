# Conversor longitud (km millas)

print("\n--- Conversor de longitudes ---")

# Menú
print("1. Kilómetros a Millas")
print("2. Millas a Kilómetros")
opcion = int(input("Elige una opción: "))

# Proceso
if opcion == 1:
    km = float(input("Ingresa los Kilómetros: "))
    mi = km * 0.621371
    print(f"{km} km son equivalentes a {mi:.2f} millas")
elif opcion == 2:
    mi = float(input("Ingresa las Millas: "))
    km = mi / 0.621371
    print(f"{mi} millas son equivalentes a {km:.2f} km")
else:
    print("Opción no válida")