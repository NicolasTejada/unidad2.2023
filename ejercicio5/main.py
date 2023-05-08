from manejadorPlanes import ManejadorPlanes
from u2ejercicio5.clasePlanAhorro import PlanAhorro

def menu():
    print('Menu Registros Metereologicos')
    print('1- Actualizar Valor Plan  ')
    print('2- Listar los planes menores a un valor .')
    print('3- Monto para licitar ')
    print('4- Modificar Cuotas  para licitar ')
    print('0- Salir')
    op=input('Ingrese la opcion elegida: ')


    return op



if __name__=='__main__':

    mp=ManejadorPlanes
    mp.testPlanes()

    op=menu()

    while op != 0:
        if op == 1:
            val=input('Ingrese el codigo del plan ')
            mp.actuValor(val)
        elif op == 2:
            valor=input('Ingrese un valor ')
            mp.planesMenor(valor)

        elif op == 3: 
            print('Monto para licitar {}'.format(PlanAhorro.montoLicitar))
        elif op== 4:
            mp.modificarCuotas()    
        elif op == 0:
            break
        
        else: print('La opcion ingresada no es correcta ')