class ViajeroFrecuente():
    __num_viajero=0
    __dni=0
    __nombre=""
    __apellido=""
    __millasAcum=0

    def __init__(self, numero, dni, nombre, apellido, millas):
        self.__num_viajero= numero
        self.__dni= dni
        self.__nombre= nombre
        self.__apellido =apellido
        self.__millasAcum=millas
        pass

    def getnumViajero(self):
        return self.__num_viajero

    def getcantidadTotalMillas(self):
        return self.__millasAcum

    
    def canjearMillas(self, millCanjear):
        if self.__millasAcum >= millCanjear :
            self.__millasAcum = self.__millasAcum - millCanjear
            return self.__millasAcum
        else:
             print('La cantidad de millas a canjear es mayor a la cantidad de millas acumuladas')
    
    def __gt__(self,otro):
        return ViajeroFrecuente(self.__millasAcum > otro.__millasAcum)

    def __add__(self,valor):
        return ViajeroFrecuente(self.__millasAcum + valor)

    def __sub__(self, valor):
        return ViajeroFrecuente(self.__millasAcum - valor)
