from collections import deque

# deque = para usar una cola que NO es lo mismo que una lista


class Banco:
    def __init__(self):
        self.cola = deque()

    def agregar_clientes(self):
        nombre = input("Ingrese el nombre del cliente: ")
        self.cola.append(nombre)
        print(f"Cliente {nombre} agregado a la cola, espere su turno.")

    def atender_cliente(self):
        if self.cola:
            cliente = self.cola.pop()
            print(f"Momento de atender al cliente: {cliente}")
        else:
            print("No hay clientes en la cola.")

    def cliente_siguiente(self):
        if self.cola:
            print(f"Siguiente cliente presentarse en la sala: {self.cola[0]}")
        else:
            print("No hay clientes en la cola.")


# Ejemplo de uso
banco = Banco()

while True:
    print("\n--- Menú del banco ---")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Ver siguiente cliente")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        banco.agregar_clientes()
    elif opcion == "2":
        banco.atender_cliente()
    elif opcion == "3":
        banco.cliente_siguiente()
    elif opcion == "4":
        print("Saliendo del sistema de turnos...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
