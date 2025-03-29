from Nodo import *
class ListaEnlazada():  
   def __init__(self):
      self.__inicio = None
      self.__fin    = None
   
   def esta_vacia(self):
      return not self.__inicio
   
   def adicionarFinal(self,n:Nodo):
      if self.esta_vacia():
         n.get_dato().set_id(1) 
         self.__inicio = self.__fin = n 
      else:
         n.get_dato().set_id(self.__fin.get_dato().get_id() + 1)
         self.__fin.set_dir_sig(n)
         self.__fin = n
   def buscar_por_id(self, id_buscar: int):
      aux = self.__inicio
      while aux:
            if aux.get_dato().get_id() == id_buscar:
               return aux.get_dato()
            aux = aux.get_dir_sig()
      return None  # Retorna None si no se encuentra

   def eliminar_por_id(self, id_eliminar: int):
      if self.esta_vacia():
            print("Lista vacía, no se puede eliminar.")
            return
      aux = self.__inicio
      ant = None
      while aux:
            if aux.get_dato().get_id() == id_eliminar:
               if ant is None:  # Si es el primer nodo
                  self.__inicio = aux.get_dir_sig()
                  if self.__inicio is None:  # Si la lista quedó vacía
                        self.__fin = None
               else:
                  ant.set_dir_sig(aux.get_dir_sig())
                  if aux == self.__fin:  # Si es el último nodo
                        self.__fin = ant
               print(f"Cliente con ID {id_eliminar} eliminado correctamente.")
               self.reasignar_ids()
               return
            ant = aux
            aux = aux.get_dir_sig()
      print(f"Cliente con ID {id_eliminar} no encontrado.")
   def reasignar_ids(self):
      aux = self.__inicio
      nuevo_id = 1
      while aux:
            aux.get_dato().set_id(nuevo_id)
            nuevo_id += 1
            aux = aux.get_dir_sig()

   def mostrar(self):
      if self.esta_vacia():
         print("Lista Vacia")
      else:
         aux = self.__inicio
         while True:
            if not aux:
               break
            else:
               aux.get_dato().mostrar()
               aux = aux.get_dir_sig()   
