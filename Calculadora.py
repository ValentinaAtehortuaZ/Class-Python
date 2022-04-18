from ipaddress import summarize_address_range
from mimetypes import init
from pdb import Restart


class Calculadora:

    def __init__(self,num1,num2):

        self.num1=num1
        self.num2=num2

        # Los metodos de una clase pueden acceder a los atributos de esta

    def sumar(self):
       return(self.num1+self.num2)

    def restar(self):
       return(self.num1-self.num2)

    def multiplicar(self):
       return(self.num1*self.num2)

    def dividir(self):
       return(self.num1/self.num2)

 
   



