#2. Crea un script llamado tabla.py que realice las siguientes tareas:
#   Debe tomar 2 argumentos, ambos numeros positivos del 1 al 9, sino mostrará un error.
#   El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas
#   En caso de no reducir uno o ambos argumentos, debe mostrar información acerca de como utilizar el script
#   El script contendrá un bucle for que itere el numero de veces del primer argumento
#   Dentro del segundo for ejecuta una instruccion print(" * ", end="),(end=" evita el salto de linea)
#   Ejecuta el codigo y observa el resultado
#Ahora intenta deducir donde y como añadir otra instrucción print para dibujar una tabla
#Recordatorio: Los argumentos se envia como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberas indicarlas entre comillas doble "esto es un argumento". Para capturar los argumentos debes utilizar el modulo sys y su lista argv:
# import sys 
# print(sys.argv) #argumentos enviados

import sys

if len(sys.argv)==3: #Siempre es el nombre del fichero
    filas=int(sys.argv[1]) # Como si fuera una lista
    columnas=int(sys.argv[2])

    if filas<1 or filas>9 or columnas<1 or columnas>9 :
        print("Error - Filas o columnas incorrectos")
        print("Ejemplo: tabla.py [1-9] [1-9]")
    else:
        #Aqui empieza la logica
        for f in range(filas):
            print()
            for c in range(columnas):
                print(" * ",end='') #El end evitara a que haya el salto de linea

else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9] [1-9]")
            
    