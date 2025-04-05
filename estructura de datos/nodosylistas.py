class Persona:
    def __init__(self, id, nombre, apellido, direccion, edad):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__edad = edad

    # Métodos Get
    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def get_apellido(self): return self.__apellido
    def get_direccion(self): return self.__direccion
    def get_edad(self): return self.__edad

class Nodo:
    def __init__(self, persona):
        self.__persona = persona
        self.__siguiente = None

    def get_persona(self): return self.__persona
    def get_siguiente(self): return self.__siguiente
    def set_siguiente(self, nodo): self.__siguiente = nodo

class ListaEnlazada:
    def __init__(self):
        self.__cabeza = None

    def agregar(self, persona):
        nuevo_nodo = Nodo(persona)
        if not self.__cabeza:
            self.__cabeza = nuevo_nodo
        else:
            actual = self.__cabeza
            while actual.get_siguiente():
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo_nodo)

    def mostrar(self):
        actual = self.__cabeza
        while actual:
            p = actual.get_persona()
            print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()}, Apellido: {p.get_apellido()}, Dirección: {p.get_direccion()}, Edad: {p.get_edad()}")
            actual = actual.get_siguiente()

    def buscar_por_id(self, id):
        actual = self.__cabeza
        while actual:
            if actual.get_persona().get_id() == id:
                return actual.get_persona()
            actual = actual.get_siguiente()
        return None

    def modificar_por_id(self, id, nuevo_nombre=None, nuevo_apellido=None, nueva_direccion=None, nueva_edad=None):
        actual = self.__cabeza
        while actual:
            persona = actual.get_persona()
            if persona.get_id() == id:
                if nuevo_nombre:
                    persona._Persona__nombre = nuevo_nombre
                if nuevo_apellido:
                    persona._Persona__apellido = nuevo_apellido
                if nueva_direccion:
                    persona._Persona__direccion = nueva_direccion
                if nueva_edad is not None:
                    persona._Persona__edad = nueva_edad
                return True
            actual = actual.get_siguiente()
        return False

if __name__ == "__main__":
    lista = ListaEnlazada()

    lista.agregar(Persona(1, "Juan", "Pérez", "Calle 123", 30))
    lista.agregar(Persona(2, "María", "Gómez", "Avenida 456", 25))
    lista.agregar(Persona(3, "Carlos", "López", "Boulevard 789", 40))
    lista.agregar(Persona(4, "Ana", "Martínez", "Calle 321", 22))

    print("\nLista de Personas:")
    lista.mostrar()

    print("\nModificando persona con ID 2 (María)...")
    if lista.modificar_por_id(2, nuevo_nombre="María Elena", nuevo_apellido="Ramírez", nueva_direccion="Nueva dirección 999", nueva_edad=28):
        print("Persona modificada con éxito.")
    else:
        print("No se encontró a la persona con ese ID.")

    print("\nLista de Personas después de la modificación:")
    lista.mostrar()
