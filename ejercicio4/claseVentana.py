

class Ventana():
    __Titulo=""
    __VertiseSupIzqX=00
    __VertiseSupIzqy=00
    __VertiseInfDerex=00
    __VertiseInfDerey=00

    def __init__(self,Titulo,supx=0,supy=0,infx=500,infy=500):
        self.__Titulo=Titulo
        if supx<infx:
            if supx>0:
                self.__VertiseSupIzqX=supx
        if supy<infy:
            if supy>0:
                self.__VertiseSupIzqy=supy
        if infx<=500:
            self.__VertiseInfDerex=infx
        if infy<=500:
            self.__VertiseInfDerey=infy
        pass
    def getTitulo(self):
        return self.__Titulo

    def alto(self):
        alto= self.__VertiseSupIzqy +  self.__VertiseInfDerey
        return alto
    def ancho(self):
        ancho= self.__VertiseSupIzqX + self.__VertiseInfDerex
        return ancho
    
    def mostrar(self):
        print('Ventana: {} vertice superior: x:{},y:{}, vertice inferior: x:{}, y:{}'.format(self.__Titulo, self.__VertiseSupIzqX, self.__VertiseSupIzqy, self.__VertiseInfDerex, self.__VertiseInfDerey))
   
    def moverDerecha(self, valor=1):
        superior= self.__VertiseSupIzqX + valor
        if superior>0:
            self.__VertiseSupIzqX=superior

        inferior=self.__VertiseInfDerex + valor
        if inferior<500:
            self.__VertiseInfDerex=inferior
    
    def moverIzquierda(self, valor=1):
        superior= self.__VertiseSupIzqX - valor
        if superior>0:
            self.__VertiseSupIzqX=superior

        inferior=self.__VertiseInfDerex - valor
        if inferior<500:
            self.__VertiseInfDerex=inferior
    
    def subir(self, valor=1):
        superior= self.__VertiseSupIzqy - valor
        if superior>0:
            self.__VertiseSupIzqy=superior

        inferior= self.__VertiseInfDerey - valor
        if inferior<500:
            self.__VertiseInfDerey=inferior

    def bajar(self, valor=1):
        superior= self.__VertiseSupIzqy + valor
        if superior>0:
            self.__VertiseSupIzqy=superior

        inferior= self.__VertiseInfDerey + valor
        if inferior<500:
            self.__VertiseInfDerey=inferior

