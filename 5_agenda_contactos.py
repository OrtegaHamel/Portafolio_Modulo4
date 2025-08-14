# Agenda muy simple usando diccionarios

agenda = {
    "Ana":   {"tel": "5551234", "email": "ana@mail.com"},
    "Luis":  {"tel": "5554321", "email": "luis@mail.com"}
}

print("\n--- Agenda de contactos ---")
while True:
    print("\n 1. Ver todos")
    print("2. Buscar")
    print("3. Agregar")
    print("4. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        for nombre, datos in agenda.items():
            print(f"{nombre} -> {datos}")
    elif opcion == "2":
        nom = input("Nombre a buscar: ")
        if nom in agenda:
            print(agenda[nom])
        else:
            print("No encontrado")
    elif opcion == "3":
        nom = input("Nombre: ")
        tel = input("Teléfono: ")
        mail = input("Email: ")
        agenda[nom] = {"tel": tel, "email": mail}
        print("Contacto agregado")
    elif opcion == "4":
        break
    else:
        print("Opción no válida")