#ERRORES
#print("Hola"
#file "<ipython-input-1-8bc9f174855>", line 1
#print("")
#pint("Hola")

#EXCEPCIONES
#n = float(input("Introduce un numero: "))
#m=4
#print("{}/{}={}".format(n,m,n/m))
#try:
#    n = float(input("Introduce un numero: "))
#    m=4
#    print("{}/{}={}".format(n,m,n/m))
#except:
#    print("Ha ocurrido un error, introduce bien el numero")

while(True):
    try: #es para capturar cualquier error dentro de un bloque de instrucciones
        n = float(input("Introduce un numero: "))
        m=4
        print("{}/{}={}".format(n,m,n/m))
        #Importante romper la iteraccion si todo ha salido bien
    except: #Para definir el codigo excepcional
        print("Ha ocurrido un error, introduce bien el numero")
        #excepciones permite un bloque de codigo else al except
    else: #Para definir el codigo que se ejecutara si no ocurre error
        print("Todo ha funcionado correctamente")
        break 
    finally: #Para definir el codigo que se ejecutara al final haya o no error
        print("Fin de la iteracion")
    
#MULTIPLES EXCEPCIONES
#try:
#    n=input("Introduce un numero: ")
#    5/n
#except Exception as e:
#    print( type (e.__name__))

try:
    n=float(input("Introduce un numero: "))
    5/n
except TypeError:
    print("No se puede dividir el numero por una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un numero")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro numero")
except Exception as e:
    print( type (e.__name__))

#INVOCACION DE EXCEPCIONES
def mi_funcion(algo=None):
    if algo is None: # o sino algo==None
        print("Error! Nos permite un valor nulo")
mi_funcion()
        
def mi_funcion(algo=None):
    try:
        if algo is None: # o sino algo==None
            raise ValueError("Error! Nos permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepcion)")
mi_funcion()        


#1. Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion
try:
    n=10/0
    print("10/0 = ", n)
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
else:
    print("Es correcto")
finally:
    print("La correccion")

#2. Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion:

try:
    lista=[1,2,3,4,5]
    print("lista[10] ",lista[10])
except IndexError:
    print("Hay un error debido a que no hay numeros ubicados en la lista")
 
#3. Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion:
try:
    colores={'rojo':'red','verde':'green','negro':'black'}
    print(colores['blanco'])
except KeyError:
    print("Error! No existe el valor ingresado en el diccionario")

#4. Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion:
try:
    print("20"+15)
except TypeError:
    print("Tiene que ingresar un numero y lo que usted ingreso fue una cadena de texto")

#5. Realiza una funcion llamada agregar_una_vez() que reciba una lista y un elemento. La funcion debe añadir el elemento al final con la condicion de no repetir ningun elemento. Ademas, si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar
#       Error: Imposible añadir elementos duplicados => [elemento].
#Prueba de agregar los elementos 10,-2,"Hola" a la lista de elementos con la funcion una vez la has creado y luego muestra su contenido.
# NOTA: Puedes utilizar la sintaxis elemento in lista
elementos=[1,5,-2]
def agregar_una_vez(lista,el):
    try:
        if el in lista:
            raise ValueError()
        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados => {} ".format(el))
    
agregar_una_vez(elementos,10)
agregar_una_vez(elementos,-2)
agregar_una_vez(elementos,"Hola")
print(elementos)