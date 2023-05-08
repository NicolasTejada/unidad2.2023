import numpy as np

from claseAlumnos import Alumno

class ArregloNumpy:
    __cantidad=0
    __dimension=0
    __incremento=5


    def __init__(self, dimension, incremento=5):
        self.__Alumnos=np.empty(dimension, dtype=Alumno)
        self.__cantidad=0
        self.__dimension=dimension

    def agregarAlumno(self, unAlumno):
        if self.__cantidad== self.__dimension:
            self.__cantidad+=self.__incremento
            self.__Alumnos.resize(self.__cantidad)
        self.__Alumnos[self.__cantidad]=unAlumno
        self.__cantidad+=

        
