class Alumno:
    __dni=00
    __apellido=""
    __nombre=""
    __carrera=""
    __añoquecursa=0

    def __init__(self, dni, ape, nom, carrer, año):
        self.__dni=dni
        self.__apellido=ape
        self.__nombre=nom
        self.__carrera=carrer
        self.__añoquecursa=año
        pass