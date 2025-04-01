# agenda.py - Agenda de Contactos

# Diccionario para almacenar los contactos
agenda = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado.")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Teléfono de {nombre}: {agenda[nombre]}")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos():
    if agenda:
        print("Lista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    else:
        print("La agenda está vacía.")

def menu():
    while True:
        print("\n📌 Menú de Agenda:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            mostrar_contactos()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu()
