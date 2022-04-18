class Personaje:
    #Constructor- Método/Funcion especial encargada de inicializar los atributos de mi clase.


    def __init__(self,name,type,house):

        #Creamos los atributos de la clase
        #atributos=datos=variables

        self.name=name
        self.type=type
        self.house=house

    #Declaro los metodos o funciones de mi clase (todas las funciones en python empiezan en minuscula, son verbos y empiezan din def)
    def saludar(self):
        print("Hi, what's up?")