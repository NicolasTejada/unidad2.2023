import csv

from clasePlanAhorro import PlanAhorro



class ManejadorPlanes():
    __ListaPlanes=None

    def __init__(self):
        self.__ListaPlanes=[]

    def agregarPlan(self,plan):
        self.__ListaPlanes.append(plan)

    def testPlanes(self):
        archivo=open('planes.csv')
        reader= csv.reader(archivo, delimiter=';')

        for fila in reader:
            cod=int(fila[0])
            mod=str(fila[1])
            valor=float(fila[2])
            cTotal=int(fila[3])
            cLicitar=int(fila[4])

            unPlan=PlanAhorro(cod,mod,valor,cTotal,cLicitar)
            self.agregarPlan(unPlan)
        archivo.close()

    def getPlan(self, codigo):
        for i in self.__ListaPlanes:
            if self.__ListaPlanes[i].__Codigo == codigo:
                return self.__ListaPlanes[i]

    def actuValor(self, codigo):
        plan=self.getPlan(codigo)
        print('Modelo Y version {}'.format(plan.getModelo))
        valor= input("Ingrese el nuevo valor: ")

        plan.setValor(valor)

        print('el valor se actualizo a: {}'.format(plan.getValor()))
    
    def planesMenor(self, valor):
        planmenorvalor=[]
        for i in self.__ListaPlanes:
            if self.__ListaPlanes[i].getValor < valor :
                planmenorvalor.append(self.__ListaPlanes[i])
        print('Plan {} Modelo y version{}'.format(planmenorvalor.getCod(), planmenorvalor.getModelo())) 
    
    def modificarCuotas(self, cuotas):
            cod=int(input('Ingrese el codigo del plan a modificar'))

            plan=self.getPlan(cod)
            plan.setCuotas

            