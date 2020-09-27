#TUPLAS
tupla=(100,"Hola",[1,2,3,4],-50)
print(tupla)
print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])#aqui me manda lo que esta dentro de la lista
print(len(tupla))
print(len(tupla[2]))
#Index para buscar un elemento y saber su posicion
print(tupla.index(100))#sirve para buscar
print(tupla.index("Hola"))
#print(tupla.index("Otro"))#No te da porque no se encuentra
print(tupla.count(100))
print(tupla.count('Algo'))
tupla=(100,100,100,50,10)
print(tupla.count(100))

#CONJUNTOS
conjunto=set()
print(conjunto)
conjunto={1,2,3}
print(conjunto)
conjunto.add(4)
print(conjunto)
conjunto.add(0)
print(conjunto)
conjunto.add('H')
print(conjunto)
conjunto.add('A')
conjunto.add('Z')
print(conjunto)
#ejemplo
grupo={'Hector','Juan','Mario'}
print('Hector'in grupo)
print('Maria'in grupo)
print('Hector'not in grupo)

test={'Hector','Hector','Hector'}
print(test)
l=[1,2,3,3,2,1]
print(l)
c=set(l)
print(c)
l=list(c)
print(l)
l=[1,2,3,3,2,1]
l=list(set(l))
print(l)
s="Al pan pan y al vino vino"
set(s)
print(s)
print(set(s))

#Diccionarios
vacio={}
print(vacio)
type(vacio)
print(type(vacio))
colores={'amarillo':'yellow','azul':'blue','verde':'green'}
print(colores)
print(colores["azul"])
print(colores["amarillo"])
numeros={10:'diez',20:'veinte'}
print(numeros[10])
colores['amarillo']='white'
print(colores)
del(colores['amarillo'])
print(colores)
edades={'Hector':27,'Juan':45,'Maria':34}
print(edades)
edades['Hector']+=1
print(edades)
print(edades['Juan']+edades['Maria'])
for edad in edades: #en este caso solo captura las claves
    print(edad)

for clave in edades:
    print(edades[clave])

for clave in edades:
    print(clave,edades[clave])    

for clave,valor in edades.items():
    print(clave,valor)
#vamos a crear una lista de personajes
personajes=[]
p={'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
personajes.append(p)
print(personajes)
p={'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p)
p={'Nombre':'Gimbli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p)
print(personajes)

for p in personajes:
    print(p['Nombre'],p['Clase'],p['Raza'])

#PILAS Y COLAS
#es una coleccion de elementos ordenados
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)
#PILAS Y COLAS
#es una coleccion de elementos ordenados
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)
print(pila.pop())
n=pila.pop()
print(n)
print(pila) 
#print(pila.pop())
#print(pila.pop())
#print(pila.pop())
#print(pila.pop())

#colas
#es una coleccion donde el primer elemnto ingresa es el primero en salir
from collections import deque
cola = deque()
print(cola)
cola=deque(['Hector','Juan','Miguel'])
print(cola)
cola.append(['Maria'])
cola.append(['Arnaldo'])
print(cola)
cola.popleft()
print(cola)
p=cola.popleft()
print(cola)
#1. Realiza un programa que siga las siguientes instrucciones:
#   Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#   Crea un conjunto llamado administradores con los administradores Juan y Marta
#   Borra al administrador Juan del conjunto de administradores
#   Añade a Marcos como un nuevo administrador, pero mo lo borres del conjunto de usuarios
#   Muestra todos los usuarios por pantalla de forma dinamica, ademas debes indicar cada usuario es administrador o no
#NOTA: Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista. También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento
usuario={'Marta','David','Elvira','Juan','Marcos'}
administradores={'Juan','Marta'}
print(usuario,administradores)
administradores.remove('Juan')
print(administradores)
administradores.add('Marcos')
print(administradores)
print(usuario)

for dinamica in usuario:
    print(dinamica)
#Esta mal verificar la correccion
for usuarios in usuario:
    if usuarios == administradores:
        print(usuarios,' Es admin')
    else:
        print(usuarios,' No es admin')


#Correccion
usuario={'Marta','David','Elvira','Juan','Marcos'}
administradores={'Juan','Marta'}
administradores.discard('Juan')
print(administradores)
administradores.add('Marcos')
print(administradores)

for usuarios in usuario:
    if usuarios in administradores:
        print(usuarios," es admin")
    else:
        print(usuarios," no es admin")


# 2. Durante el desarrolo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadistica base 2, debes cumplir las siguientes condiciones:
#   El caballero tiene doble vida y defensa que un guerrero
#   El guerrero tiene el doble ataque y alcance que un caballero
#   El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y doble de su alcance
#   Muestra como quedan las propiedades de los tres personajes
caballero={'vida':2,'ataque':2,'defensa':2,'alcance':2}
guerrero={'vida':2,'ataque':2,'defensa':2,'alcance':2}
arquero={'vida':2,'ataque':2,'defensa':2,'alcance':2}
print("Caballero: ",caballero)
caballero['vida']=guerrero['vida']*2
caballero['defensa']=guerrero['defensa']*2
print("Caballero en aumento: \t",caballero)
print("Guerrero: ",guerrero)
guerrero['ataque']=caballero['ataque']*2
guerrero['alcance']=caballero['alcance']*2
print("Guerrero en aumento: \t",guerrero)
print("Arquero: ",arquero)
arquero['vida']=guerrero['vida']
arquero['ataque']=guerrero['ataque']
arquero['defensa']=guerrero['defensa']/2
arquero['alcance']=guerrero['alcance']*2
print("Arquero en aumento: \t",arquero)
print("-------------------------------------------------------\n")
print("Caballero en aumento: \t",caballero)    
print("Guerrero en aumento: \t",guerrero)
print("Arquero en aumento: \t",arquero)

#3. Durante la planificacion de un proyecto se han acortado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad(Cuanto menor es el numero de orden, mas prioridad)
# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenada pero sin los numeros de orden?
# Pista. Para ordenar automaticamente una lista es posible utilizar el metodo .sort()
tareas = [[6,'Distribución'],[2,'Diseño'],[1,'Concepción'],[7,'Mantenimiento'],[4,'Producción'],[3,'Planificación'],[5,'Pruebas']]
print("\n\n\n==Tareas desordenadas==\n")
for tarea in tareas:
    print(tarea[0],tarea[1])

from collections import deque
tareas.sort(reverse=False) #Puede funcionar sin agregar en el parentesis
print(tareas)
print("\n\n\n=================Tareas ordenadas===================\n")
for ordenado in tareas:
    print(ordenado[0],ordenado[1])


