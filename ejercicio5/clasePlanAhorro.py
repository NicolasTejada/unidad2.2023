
class PlanAhorro():
    __Codigo=00
    __ModeloyVersion= ""
    __Valor=00
    __CTotales=0
    __CnesLicitar=0
    
    def __init__(self, cod, mod, valor, cuotas, CLicitar):
        self.__Codigo=cod
        self.__ModeloyVersion=mod
        self.__Valor=valor
        self.__CTotales=cuotas
        self.__CnesLicitar=CLicitar

        
    def __str__(self):
        return ('{}{}{}{}{}'.format(self.__Codigo,self.__ModeloyVersion,self.__Valor, self.__CTotales, self.__CnesLicitar))

    def setValor(self, val):
        self.__Valor=val  
    def getCod(self):
        return self.__Codigo
    def getValor(self):
        return self.__Valor

    def getModelo(self):
        return self.__ModeloyVersion
    
    def setCuotas(self, cuotas):
        self.__CnesLicitar=cuotas
    
    @classmethod
    def valorCuota(cls):
        cuota=(cls.__Valor/cls.__CTotales)+cls.__Valor*0.10
        return cuota

    @classmethod
    def montoLicitar(cls):
        monto=(cls.__CnesLicitar)*cls.valorCuota
        return monto
    


