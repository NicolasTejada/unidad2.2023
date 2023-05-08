

class Registro():
    __Temperatura = 0
    __Humedad= 0 
    __PresionAtmosferica = 0

    def __init__(self, temp, hume, presion ):
        self.__Temperatura = temp
        self.__Humedad = hume
        self.__PresionAtmosferica = presion
        pass


    def __str__(self):
        return '({}{}{})'.format(self.__Temperatura, self.__Humedad, self.__PresionAtmosferica)

    def getTemperatura(self):
        return self.__Temperatura
    
    def getHumedad(self):
        return self.__Humedad
    
    def getPresion(self):
        return self.__PresionAtmosferica