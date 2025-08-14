# Formulario que pide datos personales y los muestra

print("\n--- Formulario de registro ---")

nombre   = input("Nombre: ")
edad     = int(input("Edad: "))
estatura = float(input("Estatura en metros: "))
estudiante = input("¿Eres estudiante? (si/no): ").strip().lower() == "si"

print("\n--- Datos capturados ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura} m")
print(f"Estudiante: {estudiante}")