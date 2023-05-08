import csv
from viajerosfrecuentes import ViajeroFrecuente 


class manejadorViajeros():
    __listaViajeros = []

    def __init__(self):
        self.__listaViajeros=[]
    def agregarViajero(self,unviajero):
        self.__listaViajeros.append(unviajero)
    
    def buscarViajero(self, clave):
        for indice, viajero in enumerate(self.__listaViajeros):
            if ViajeroFrecuente.getnumViajero == clave:
                return indice

    def testViajeros(self):
        archivo = open('u2ejercicio2\viajeros.csv')
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
    
    