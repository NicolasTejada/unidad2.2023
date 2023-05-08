import csv

from viajerosfrecuentes import * 

from manejadorviajeros import *


def menu():
    print('Menu viajeros ')
    print('1- Consultar la Cantidad de Millas ')
    print('2- Acumular Millas')
    print('3- Canjear Millas ')
    print('0- Salir')
    op=input('Ingrese la opcion elegida: ')


    return op
if __name__=='__main__':

   
    mv= manejadorViajeros()
    mv.testViajeros()
    v=int(input('Ingrese el numero del viajero'))
    indice= mv.buscarViajero(v)
    
    op=menu()
    
    while op != 0:
        if op == 1:
            print('La cantidad total de millas acumuladas es de: {}' .format(mv.__listaViajeros[indice].getcantidadTotalMillas()))
        elif op == 2:
            m=input('Ingrese las millas recorridas' )
            print('millas acumuladas {}'.format(mv.__listaViajeros[indice].acumularMillas()))
        elif op == 3: 

            m=input('Ingrese las millas a canjear' )
            print('millas canjeadas {}'.format(mv.__listaViajeros[indice].canjearMillas(m)))

        elif op == 0:
            break
        
        else: print('La opcion ingresada no es correcta ')
