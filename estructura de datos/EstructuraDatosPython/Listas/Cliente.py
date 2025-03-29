class Cliente:
    #constructor
    def __init__(self):
        self.__id = 0
        self.__nombres = ""
        self.__apellidos = ""
        self.__edad = 0
        self.__sexo = ""
    #get
    def get_id(self)->int:
        return self.__id
    def get_nombres(self)->str:
        return self.__nombres
    def get_apellidos(self)->str:
        return self.__apellidos
    def get_edad(self)->int:
        return self.__edad
    def get_sexo(self)->str:
        return self.__sexo
    #set
    def set_id(self,id:int)->None:
        self.__id = id
    def set_nombres(self,nombres:str)->None:
        self.__nombres = nombres
    def set_apellidos(self,apellidos:str)->None:
        self.__apellidos = apellidos
    def set_edad(self,edad:int)->None:
        self.__id = id
    def set_sexo(self,sexo:str)->None:
        self.__sexo = sexo
    #acciones
    def es_mayor_edad(self, edad_mayor):
        return self.__edad >= edad_mayor
    def leer(self):
        self.__nombres   = input("Nombres:")
        self.__apellidos = input("Apellidos:")
        self.__edad      = int(input("Edad:"))
        self.__sexo      = input("Sexo m-masculino,f-femenino:")

    def mostrar(self):
        print(f"{self.__nombres} {self.__apellidos} {self.__edad} {self.__sexo}")

    