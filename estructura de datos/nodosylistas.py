class Persona:
    def __init__(self, nombre, apellido, direccion, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__edad = edad

    # Métodos Get
    def get_nombre(self): 
      return self.__nombre
    def get_apellido(self): 
      return self.__apellido
    def get_direccion(self): 
      return self.__direccion
    def get_edad(self): 
      return self.__edad

class Nodo:
    def __init__(self, persona):
        self.__persona = persona  # Guarda el objeto Persona
        self.__siguiente = None  # Enlace al siguiente nodo

    def get_persona(self): return self.__persona
    def get_siguiente(self): return self.__siguiente
    def set_siguiente(self, nodo): self.__siguiente = nodo

class ListaEnlazada:
    def __init__(self): self.__cabeza = None

    def agregar(self, persona):
        """ Agrega un nodo al final de la lista enlazada """
        nuevo_nodo = Nodo(persona)
        if not self.__cabeza:
            self.__cabeza = nuevo_nodo
        else:
            actual = self.__cabeza
            while actual.get_siguiente():  # Recorre hasta el último nodo
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo_nodo)  # Enlaza el nuevo nodo

    def mostrar(self):
        actual = self.__cabeza
        while actual:
            p = actual.get_persona()
            print(f"Nombre: {p.get_nombre()}, Apellido: {p.get_apellido()}, Dirección: {p.get_direccion()}, Edad: {p.get_edad()}")
            actual = actual.get_siguiente()

    def buscar(self, nombre):
        actual = self.__cabeza
        while actual:
            if actual.get_persona().get_nombre() == nombre:
                return actual.get_persona()
            actual = actual.get_siguiente()
        return None

# Pruebas
if __name__ == "__main__":
    lista = ListaEnlazada()

    # Agregamos varias personas (creando varios nodos)
    lista.agregar(Persona("Juan", "Pérez", "Calle 123", 30))
    lista.agregar(Persona("María", "Gómez", "Avenida 456", 25))
    lista.agregar(Persona("Carlos", "López", "Boulevard 789", 40))
    lista.agregar(Persona("Ana", "Martínez", "Calle 321", 22))

    print("\nLista de Personas:")
    lista.mostrar()

    print("\nBuscando a Carlos...")
    persona = lista.buscar("Carlos")
    if persona:
        print(f"Encontrado: {persona.get_nombre()} {persona.get_apellido()}, {persona.get_direccion()}, {persona.get_edad()} años")
    else:
        print("No se encontró a la persona.")
