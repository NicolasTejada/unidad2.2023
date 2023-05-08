from manejadorRegistros import manejadorRegistro


def menu():
    print('Menu Registros Metereologicos')
    print('1- Mostrar para cada variable el día y hora de menor y mayor valor. ')
    print('2- Indicar la temperatura promedio mensual por cada hora.')
    print('3- Listado de los registros por hora ')
    print('0- Salir')
    op=input('Ingrese la opcion elegida: ')


    return op

   


if __name__=='__main__':

   
    mr= manejadorRegistro
    mr.testRegistro()
       
    op=menu()
    
    while op != 0:
        if op == 1:
            mr.mayorvalor()
        elif op == 2:
            lista= mr.promedio()
            print('Temperatura promedio por hora')
            for i in lista:
               print('hora {} temperatura {}'.format(i, lista[i]))

        elif op == 3: 

           mr.mostrarDatos()
        elif op == 0:
            break
        
        else: print('La opcion ingresada no es correcta ')