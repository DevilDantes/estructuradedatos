import os
from ListaEnlazada import *
def adicionarClientes(l)->None:
    while True:
        os.system('cls')
        print("Adicionar cliente: ")
        n = Nodo()
        n.get_dato().leer()
        l.adicionarFinal(n)
        c = int(input("Deseas continuar? Si con un 0: "))
        if c != 0:
            break

def mostrarClientes(l):
    os.system('cls')
    print("        Mostrar clientes\n Nombres     Apellidos     Edad     Sexo")   
    l.mostrar()

def eliminarCliente(l):
    id_eliminar = int(input("Ingrese el ID del cliente a eliminar: "))
    l.eliminar_por_id(id_eliminar)

def buscarCliente(l):
    id_buscar = int(input("Ingrese el ID del cliente a buscar: "))
    cliente = l.buscar_por_id(id_buscar)
    if cliente:
        print("Cliente encontrado:")
        cliente.mostrar()
    else:
        print("Cliente no encontrado.")

def main():
    l = ListaEnlazada()
    while True:
        print("\nMenú de opciones:")
        print("1. Adicionar Cliente")
        print("2. Mostrar Clientes")
        print("3. Buscar Cliente por ID")
        print("4. Eliminar Cliente por ID")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            adicionarClientes(l)
        elif opcion == 2:
            mostrarClientes(l)
        elif opcion == 3:
            buscarCliente(l)
        elif opcion == 4:
            eliminarCliente(l)
        elif opcion == 5:
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == '__main__':
    main()
