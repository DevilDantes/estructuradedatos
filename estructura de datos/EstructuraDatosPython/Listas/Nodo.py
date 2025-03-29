from Cliente import *
from Nodo import *
class Nodo():
    def __init__(self):
        self.__dato    = Cliente()
        self.__dir_sig = None

    def get_dato(self):
        return self.__dato

    def get_dir_sig(self):
        return self.__dir_sig
    
    def set_dato(self,dato):
        self.__dato = dato
  
    def set_dir_sig(self,dir_sig):
        self.__dir_sig = dir_sig

    