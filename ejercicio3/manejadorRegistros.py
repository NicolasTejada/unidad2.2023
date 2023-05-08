import csv 

from claseregistro import Registro


class manejadorRegistro():
    
    def __init__(self):
        self.__listaregistro = [[ 0.0 for _ in range(24) ] for _ in range(31)]

    def _str_(self):
        print(self.__listaregistro)
    
    def agregarRegistro(self, dia, hora, unRegistro ):
        self.__listaregistro[dia-1][hora]=unRegistro



    def testRegistro(self):
        archivo = open('registro.csv')
        reader = csv.reader(archivo,delimiter=',')
        
        for fila in reader:
            dia= int(fila[0])
            hora= int(fila[1])
            temperatura = float(fila[2])
            humedad = float(fila[2])
            presion = float(fila[2])
            
            
            unRegistro = Registro(temperatura, humedad, presion)
            self.agregarRegistro(dia,hora, unRegistro)
        archivo.close()

    def mayorvalor(self):
        temperaturaMay = 00
        humedadMay = 00
        presionMay=00
        diatemp = 0 
        horatemp= 0
        diahum =0
        horahum=0
        diapres=0
        horapres=0
        for i in range(len(self.__listaregistro)):
            for j in range(len(self.__listaregistro)):
                if object.getTemperatura() > temperaturaMay:
                    temperaturaMay = object.getTemperatura()
                    diatemp= i 
                    horatemp= j 
                if object.getHumedad > humedadMay:
                    humedadMay = object.getHumedad
                    diahum= i 
                    horahum= j
                if object.getPresion > presionMay:
                    presionMay = object.getPresion
                    diapres= i 
                    horapres= j
        print('El dia con mayor temperatura es {} a la hora {}'.format(diatemp, horatemp))
        print('El dia con mayor humedad es {} a la hora {}'. format(diahum, horahum))
        print('El dia con mayor presion es {} a la hora {}'. format(diapres, horapres))
    
    def promedio(self):
        hora=[]
        dias = 00
        for i in range(len(self.__listaregistro)):
            for j in range(len(hora)):
                if self.__listaregistro[i][j]>00:
                    hora[j] += self.__listaregistro[i][j].getTemperatura
                    dias= dias+1
        for i in range(len(hora)):
            hora[j]= hora[j]/dias
        

        return hora 

    def mostrarDatos(self):
        dia=input('Ingrese el dia')
        print('Hora   Temperatura    Humedad    Presion ')
        for i in range(len(24)):
            print('{}    {}    {}      {}  '.format(i, self.__listaregistro[dia-1][i].getTemperatura,self.__listaregistro[dia-1][i].getHumedad, self.__listaregistro[dia-1][i].getPresion)  )
