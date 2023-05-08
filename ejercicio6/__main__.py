from ManejadorViajeros import manejadorViajero

def opcion0(viajero):
    print('Adios')

def opcion1(viajero):
    print('cantidad Total de millas acumuladas:  {} '.format(mv.__listaViajeros[viajero].getcantidadTotalMillas))

def opcion2(viajero):
    millas=input('Ingrese la cantidad de millas:  ')
    mv.acumularMillas(millas, viajero)

def opcion3(viajero):
    millas=input('Ingrese la cantidad de millas:  ')
    mv.canjearMillas(viajero,millas)
    
switcher = {
 0: opcion0,
 1: opcion1,
 2: opcion2,
 3: opcion3
}
def switch(argument,mv):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(mv)


if __name__=='__main__':

    mv=manejadorViajero()
    mv.testViajeros()


    print('********Bienvenido*********')
    codigo=input('Ingrese el codigo del Viajero: ')

    viajero=mv.getViajero(codigo)

    
    bandera = False
    while not bandera:
         print("\nMENU DE OPCIONES")
         print("0 Salir")
         print('1- Consultar la Cantidad de Millas ')
         print('2- Acumular Millas')
         print('3- Canjear Millas ')
         opcion = int(input ('Ingrese una opcion:'))
         switch(opcion, viajero)
         bandera = int(opcion)== 0