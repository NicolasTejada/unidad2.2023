import csv 

from claseViajerosFrecuentes import ViajeroFrecuente


class manejadorViajero():
    __listaViajeros = []

    def __init__(self):
        self.__listaViajeros=[]
    def agregarViajero(self,unviajero):
        self.__listaViajeros.append(unviajero)
    
    def getViajero(self, clave):
        for indice, viajero in enumerate(self.__listaViajeros):
            if viajero.getnumViajero == clave:
                return indice
    
    def acumularMillas(self, valor, viajero):
        self.__listaViajeros[viajero] = self.__listaViajeros[viajero] + valor
    
    def canjearMillas(self, viajero, valor ):
        self.__listaViajeros[viajero] = self.__listaViajeros[viajero] - valor 


    def testViajeros(self):
        archivo =  open("C:/Users/Nicolas/Desktop/phyton poo/u2ejercicio6/Lista.csv")
        reader = csv.reader(archivo,delimiter=',')
        
        for fila in reader:
            
            numeroviajero = int(fila[0])
            dni = int(fila[1])
            nombre = str(fila[2])
            apellido = str(fila[3])
            millasAcumuladas = int(fila[4])
            
            unviajero = ViajeroFrecuente(numeroviajero,dni, nombre, apellido, millasAcumuladas)
            self.agregarViajero(unviajero)
        archivo.close()
    