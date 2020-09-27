#3. [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:
#   Debe tomar 1 argumento que será un número 
#   En caso de no recibir un argumento, debe mostrar información acerca de como utilizar el script.
#El objetivo del script es descomponer el numero de unidades, decenas, centenas, miles.. tal que por ejemplo si se introduce el numero:
#3647
#el programa debera devolver una descomposición linea a linea como la siguiente utilizando las tecnicas de formateo:
#0007
#0040
#0600
#3000
#Pista: Que el valor sea un numero no significa necesariamente que deba serlo para formatearlo. Necesitara jugar muy bien con los indices y realizar muchas conversiones entre tipos cadenas, numeros y viceversa
import sys
if len(sys.argv)==2:
    numero=int(sys.argv[1])
    if numero<0 or numero>9999:
        print("Error - Numeros es incorrecto")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        #Aqui va la logica
        cadena=str(numero)
        longitud=len(cadena)

        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud-1-i]) * 10 ** i ))
            

else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: descomposicion.py [0-9999]")    