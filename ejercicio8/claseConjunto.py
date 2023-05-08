import numpy as np


class conjunto:
    __dimension=0

    def __init__(self, dim):
        self.__conjunto= np.empty(dim,int)
        pass

    def agregaentero(self, entero):
        self.__listenteros.append(entero)


    def __radd__(self, otroConjunto):
        ConjUnion=np.empty(self.__dimension + otroConjunto.__dimension)

        for i in ConjUnion:
            for i in 