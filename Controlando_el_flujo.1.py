#El uso de IF
if not False:
    print("Se cumple la función")
    print("También se muestre este print")
#Otro ejemplo
print("Otro ejemplo")
a=5
if a==2:
    print("a vale 2")
if a==5:
    print("a vale ",a)
#Otro ejemplo
print("Otro ejemplo")
a=5
b=10
if a==5:
    print("a vale ",a)
    if a==5:
        print("y b vale ",b)
#Otro ejemplo
if a==5 and b==10:
    print("a vale ",a," y b vale ",b)
#Otro ejemplo
print("Otro ejemplo")
comando="OTRA COSA"
if comando=="ENTRAR":
    print("Bienvenido al sistema")
elif comando=="SALUDAR":
        print("Hola, espero que estes feliz conmigo y que me extrañes obvio..")
elif comando=="SALIR":
    print("Saliendo del sistema.......")
else:
    print("Este comando no se reconoce")   
#Otro ejemplo
print("Otro ejemplo")
nota=float(input("Introduce una nota: "))
if nota>=18 and nota<=20:
    print("Sobresaliente")
if nota<18 and nota>=14:
    print("Notable")
if nota<14 and nota>=12:
    print("Suficiente")
if nota<12 and nota>=10:
    print("Insuficiente")
if nota<12 and nota>=0:
    print("Deficiente")
else:
    print("Fuera de rango")    
        
#El uso de while
c=0
while c <= 5:
    c+=1
    print("c vale ",c)
else:
    print("Se ha completado toda la iteración y c vale",c)
 
#Otro ejemplo
print("Otro ejemplo")
c=0
while c <= 5:
    c+=1
    if c==2:
        print("Rompemos el bucle cuando c vale",c)
        break #con esto rompemos el bucle
    print("c vale ",c)
else:
    print("Se ha completado toda la iteración y c vale",c)
    
#Otro ejemplo
print("Otro ejemplo")
c=0
while c <= 5:
    c+=1
    if c==2:
        print("Rompemos el bucle cuando c vale",c)
        continue #con esto excepcionas una vuelta y sigue continuando
    print("c vale ",c)
else:
    print("Se ha completado toda la iteración y c vale",c)
#Otro ejemplo
    print("Otro ejemplo")
    print("Bienvenido al menu interactivo")
    while (True):
        print("""¿Que quieres hacer? Escribe una opción 
        1) Saludar
        2) Sumar 2 numeros
        3) Salir""")
        opcion=input()
        if opcion=='1':
            print("Hola, espero que la estes pasando bien")
        elif opcion=='2':
            a=float(input("Ingrese el primer numero: "))
            b=float(input("Ingrese el segundo numero: "))
            print("La suma es: ",a+b)
        elif opcion=='3':
                print("Hasta luego ha sido un placer ayudarte")
                break
        else:
            print("Comando desconocido, vuelve a intentarlo")

#El uso de for
numeros=[1,2,3,4,5,6,7,8,9,10]
indice=0
while (indice<len(numeros)):
    print(numeros[indice])
    indice+=1

 #Otro ejemplo
    print("Otro ejemplo")
for numero in numeros:
    print(numero)

 #Otro ejemplo   
for numero in numeros:
     numero*=10
     print(numero)
#Otro ejemplo   
print("Otro ejemplo")
indice=0
numeros=[1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice]*=10
    indice+=1
print(numeros)

#Otro ejemplo
print("Otro ejemplo")  
numeros=[1,2,3,4,5,6,7,8,9,10]
for indice,numero in enumerate(numeros):
    numeros[indice]*=10
    print(numeros)
#Otro ejemplo
print("Otro ejemplo")
cadena="Hola amigos"
for caracter in cadena:
    print(caracter)
    #Otro ejemplo
print("Otro ejemplo")
cadena2=""
for caracter in cadena:
    cadena2 += cadena * 2
    print(cadena)
    print(cadena2)
#Otro ejemplo
print("Otro ejemplo")
range(10)
for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)
#Ejercicios
print("Resolviendo los ejercicios propuestos")
#1. Realiza un programa que lea dos numeros por teclado y permita elegir 3 opciones en menu
# .Mostrar una suma de los dos numeros
# .Mostrar una resta de los numeros(el primero menos el segundo)
# .Mostrar una multiplicacion de los dos numeros
# .En caso de no introducir una opcion valida, el programa informara de que no es correcta
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))

print("Debe introducir un numero:")
print("""Que desea hacer
1) Suma
2) Resta
3) Multiplicacion""")
selecciona=input("Ingrese numero: ")
if selecciona=='1':
    print("La suma es:",num1+num2)
elif selecciona=='2':
    print("La resta es:",num1-num2)
elif selecciona=='3':
    print("La multiplicacion es:",num1*num2) 
else:
    print("Opcion incorrecta")

#2. Realiza un programa que lea un numero impar por teclado. Si el usuario no introduce un numero impar, debe repetirse el proceso hasta que lo introduzca correctamente
numimpar=0
while (True):
        print("Ingrese un numero ")
        numimpar=int(input())
        if (numimpar%2)==0:
            print("No es el numero indicado, tiene que ingre3sar un numero impar")
        elif (numimpar%2)!=0:       
                print("Este si es un numero impar")
                break
#Solucion
numimpar1=0
while numimpar1%2==0:
    numimpar1=int(input("Introduce un numero impar"))
#3. Realiza un programa que sume todos los numeros enteros pares desde el 0 hasta el 100
#sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo mas facil. El tercer parametro en la funcion range(inicio, fin, salto)indica el sato de numeros, pruebalo
n=0
suma=0
print("La suma es: ",list(range(0,101,2)))
print("La suma total va a ser: ",sum(range(0,101,2)))
for n in list(range(0,101,2)):
    suma+=n
    print("La suma es: ",suma)
print("La suma total es: ",(suma))
#solucion
#Primera forma
suma1=sum(range(0,101,2))
print("La suma es: ",suma)
#Segunda forma
numero1=0
suma11=0
while numero1<=100:
    if numero1%2==0:
        suma11+=n
    numero1+=1        
    print("La suma es: ",suma11)
print("La suma total es: ",suma11)

#4. Realiza un programa que pida el usuario cuantos numeros quiere introducir. Luego lee todo los numeros y realiza una media aritmetica  
#Esta mal :(

#numero=0
#suma=0
#cant=int(input("Cuantos numeros quieres ingresar: "))
#while cant>=0:    
 #   if cant==0:
 #       print("La cantidad no esta ingresada")
 #       break
 #   else:
 #       numero=int(input("Ingrese el numero: "))          
#       print("La suma de los numeros ingresados es: ",suma)
#        suma+=numero
       
#print("La media es: ",(suma/cant))
#Solucion
repeticion=int(input("Ingrese la cantidad de numeros que quieres introducir: "))
suma1=0
for r in range(repeticion):
    suma1+=float(input("Introduce un numero: "))    
print("Se han introducido ",repeticion," numeros en total han sumado ",suma1," y la media es: ",(suma1/repeticion))
#5. Realiza un programa que pida al usuario un numeroo del 0 al 9, y que mientras el numero no sea correcto repita el proceso. Luego debe comprobar si el numero se encuentra en la lista de numeros y notificarlo:
#Consejo La sintaxis "Valor in lista" permite comprobar facilmente si un valor se encuentra en una lista (devuelve True o False)
numeros=[1,2,3,4,5,6,7,8,9]
while True:
    numero=int(input("Ingrese un numero del 0 al 9: "))
    if numero>=0 and numero<=9:
        print("Ingreso un numero fuera de rango")
        break

if numero in numeros:
    print("El numero ",numero," se encuentra en la lista de ",numeros)
else:
    print("El numero ",numero,"NO se encuentra en la lista de ",numeros)

#6. Utilizando la funcion range() y la conversion a listas genera las siguientes listas dinamicamente
# Todos los numeros del 0 al 10 [0,1,2,,..10]
# Todos los numeros del -10 al 0 [-10,-9,-8,...,0]
#  Todos los numeros pares del 0 al 20 [0,2,4,...,20]
#  Todos los numeros impares entre -20 y 0 [-19,-17,-15,...,1]
# Todos los numeros multiples de 5 del 0 al 50 [0,5,10,..,50]
#Pista: Utiliza el tercer parametro de la funcion range(iinicio,fin,salto)
num1=list(range(0,11))
num2=list(range(-10,1))
num3=list(range(0,21,2))
num4=list(range(-19,2,2))
num5=list(range(0,51,5))
print("Todos los numeros del 0 al 10",num1)
print("Todos los numeros del -10 al 0",num2)
print("Todos los numeros pares del 0 al 20 ",num3)
print("Todos los numeros impares entre -20 y 0",num4)
print("Todos los numeros multiples de 5 del 0 al 50",num5) 

# 7. Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningun elemento en la nueva lista
lista1=["h",'o','l','a',' ','m','u','n','d','o']
lista2=["h",'o','l','a',' ','l','u','n','a']

lista3=[]
for letra in lista1:
    if letra in lista2 and letra not in lista3:
        lista3.append(letra)
    print(lista3)
print("La captura real ",lista3)    