#FUNCIONES
#Son fragmentos de codigo que se pueden ejecutar múltiples que se pueden ejecutar multiples veces
#Pueden recibir y devolver información para comunicarse con el proceso principal

#DEFINICION DE FUNCIONES
# "Hola" --> len() --> 4
def saludar():
    print("Hola! Este print se llama desde la funcion saludar()")

saludar()
def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * ",i," = ",(i*5))
dibujar_tabla_del_5()

#def test():
#   n=10
#test()
#print(n)
#n no existe en elp´roceso principal solo dentro de la funcion ya que lo hemos declarado alli, diriamos entonces que el ambito de la variable n abarca unicamente la funcion test
n=10
def test():
    print(n)

test()

def test():
    print(i)
#test()
i=10
test()

def test():
    o=5
    print(o)
test()

o=10
test()
print(o)
#En este caso en python siempre una variable igual con diferentes significados pueden tambier ocurrir aqui, entonces para evitar eso siempre es bueno que las variables sean distintas

#RETORNO DE VALORES
def test1():
    return "Una cadena retornada"
    print("Otro print")

test1()
print(test1())
c=test1()
print(c)
#c=test1()+10 #Aqui no se puede por que no se puede sumar cadena con un numero
print(c)

def test2():
    return [1,2,3,4,5]
print(test2())
print(test2()[-1])
print(test2()[1:4])
l=test2()
print(l[-1])
def test3():
    return "Una cadena ",20,[1,2,3]

test3()
print(test3())
c1,n1,l1=test3()
print(c1)
print(n1)
print(l1)

#ENVIANDO VALORES
def suma(a,b):
    return a+b;
a=int(input("Ingrese el primer numero: ")) 
b=int(input("Ingrese el segundo numero: ")) 
print(suma(a,b))

def multiplicar(x,y):
    return x*y
r=multiplicar(5,3)
print(r)

#ARGUMENTOS Y PARAMETROS
def resta(a,b):
    return a-b
print(resta(1,2))

def resta1(a=None,b=None):
    if a== None or b==None:
        print("Error, debes enviar dos numeros a la funcion")
        return
    else:
        return a-b
print(resta1(1,5))

#ARGUMENTOS POR VALOR Y REFERENCIA
def doblar_valor(numero):
    numero*=2

n=10
doblar_valor(n)
print(n)    

#def doblar_valores(numeros):
#    for i.n in enumerate(numeros):
#        numeros[i]*=2
#ns=[10,50,100]

#print(doblar_valores(ns))
#print(ns)


def doblar_valor(numero):
    return numero*2
n=10
n=doblar_valor(n)
print(n)

#NO ME SALE
#def doblar_valores(numeros):
#    for i.n in enumerate(numeros):
#        numeros[i]*=2
#ns=[10,50,100]

#doblar_valores(ns[:])
#print(ns)


#ARGUMENTOS Y PARAMETROS INDEFINIDOS
def indeterminados_posicion(*args):
    print(args)

indeterminados_posicion(5,"Hola",[1,2,3,4,5])
print(indeterminados_posicion(5,"Hola",[1,2,3,4,5]))


def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(5,"Hola",[1,2,3,4,5])
print(indeterminados_posicion(5,"Hola",[1,2,3,4,5]))
 

def indeterminados_nombre(**kwargs):
    print(kwargs)

print(indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5]))

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

print(indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5]))

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," = ",kwargs[kwarg])

print(indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5]))
#Esto es muy importante
def super_funcion(*args, **kwargs):
    t=0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminado es ",t)
    for kwarg in kwargs:
        print(kwarg," = ",kwargs[kwarg])                
print(super_funcion(10,50,-1,1,56,25,300,nombre="Hector",edad=22))

#FUNCIONES RECURSIVAS
def cuenta_atras(num):
    num-=1
    if num>0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooooooom!!")
    print("Fin de la funcion ",num)

print(cuenta_atras(9))

def factorial(num):
    print("Valor inicial --> ",num)
    if num>1:
        num=num*factorial(num-1)
    print("Valor final --> ",num)
    return num
#factorial(5)
print(factorial(5))

#FUNCIONES INTEGRADAS
#cuando se agrega el int o float practicamente lo reconoce como numero ese caracter
n = int("10") 
print(n)
f=float("10.5")
print(f)

#str es para convertir a string el numero
c="Un texto y un numero "+str(10)+ " "+str(3.14)
print(c)
#bin y hex es para convertir un numero al sistema que se necesite en reste caso al binario y al hexadecimal
bin(10)
print(bin(10))
print(hex(10))
#int + '' es para convertir el numero al sistema decimal que conocemos
print(int('0b1010',2))
print(int('0xa',16))
#abs es para convertir en valor absoluto
print(abs(-10))
print(abs(10))
#round es para redondear el numero
print(round(5.5))
print(round(5.4))
print(eval('2+5'))
#eval para evaluar el numero
n=10
print(eval('n * 10 - 5'))
#len para calcular la cadena es un convertidor 
print(len("Una cadena"))
print(len([]))
#para ayuda
help()

#1. realiza una funcion llamada area_rectangulo() que devuelva el area del cuadradp a partir de una base y una altura Calcula el area de un rectangulo de 15 de base y 10 de altura
#NOTA: el area de un cuadrado se obtiene al multiplicar la base por la altura
def area_rectangulo(base,altura):
    return base*altura
print("El area del rectangulo es: ",area_rectangulo(15,10))

#2. realiza una funcion llamada area_circulo() que devuelva el area de un circulo a partir de un radio. Calcula el area de un circulo de 5 de ancho:
#NOTA: El area de un circulo se obtiene al elevar el radio a dos y multiplicando el resultado por el numero pi. Puedes utilizar el valor 3.14159 como pi o importarlo del modulo math
import math
print(math.pi)
def area_circulo(radio):
    return math.pi*pow(radio, 2)
ancho=float(input("Ingrese aqui el ancho del circulo: "))
radio=ancho/2
print(area_circulo(radio))

#3. realiza una funcion llamada relacion() que a partir de dos numeros cumpla lo siguiente:
# Si el primer numero es mayor que el segundo, debe devolver 1
# Si el primer numero es menor que el segundo, debe devolver 1
# Si el ambos numeros son iguales, debe devolver 0
# Comprueba la relacion entre los numeros '5' y '10',"10 y 5" y "5 y 5" 
def relacion(a,b):
    if a>b or a<b:
        return 1
    else:
        return 0
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))
#4. realiza una funcion llamada intermedio() que a partir de dos numeros, devuelva su punto intermedio:
#NOTA: El numero intermedio de dos numeros corresponde a la suma de los dos numeros dividida entre 2
def intermedio(x,y):
    return (x+y)/2
print(intermedio(-12,24))
#5. realiza una funcion llamada recortar() que reciba tres parametros. El primero es el numero a recortar, el segundo es el limite inferior y el tercero el limite superior. La funcion tendra que cumplir lo siguiente:
# Devolver el limite inferior si el numero es menor que este
# Devolver el limite superior si el numero es mayor que este
# Devolver el numero sin cambios si no se supera ningun limite 
#Comprueba el resultado de recortar 15 entre los limites 0 y 10 
def recortar(numero,lim_inf,lim_sup):
    if numero<lim_sup:
        return lim_inf
    if numero>lim_sup:
        return lim_sup
    return numero

print(recortar(15,0,10))
    
#6. realiza una funcion separar() que tome una lista de numeros y devuelva dos listas ordenadas. La primera con los numeros pares y la segunda con los numeros impares:
# Ejemplo: 
# pares, impares = separar ([6,5,2,1,7])
#print(pares) #valdria [2,6]
#print(impares) #valdria [1,5,7]
numeros=[-12,84,13,20,-33,101,0]

def separar(lista):
    lista.sort()
    pares=[]
    impares=[]
    for n in lista:
        if n%2==0:
            pares.append(n)
        else:
            impares.append(n)
    return pares,impares
pares,impares=separar(numeros)
print(pares)
print(impares)
            

    

    