#CADENAS
print("Hola Mundo".upper()) #Este metodo lo devuelve a mayusculas
print("Hola Mundo".lower()) #Este metodo lo devuelve a minusculas
print("Hola Mundo".capitalize()) #Este metodo lo devuelve a mayusculas las primera letra de la frase en mayuscula
print("Hola Mundo".title()) #Este metodo lo devuelve las primeras letras en mayusculas
print("Hola Mundo".count('Mundo')) #Este metodo cuenta el caracter especifico
print("Hola Mundo".find('Mundo')) #Este metodo cuenta desde donde comienza el caracter 
print("Hola Mundo Mundo Mundo Mundo".rfind('Mundo')) #Este metodo indica el indice donde empieza el ultimo lo que va a buscar
c="100"
print(c.isdigit()) #Este metodo nos dice si es v o f si es un numero o digito 
c2="ABC1034po"
print(c2.isalnum()) #Este metodo comprueba si contiene todos los numeros alfanumericos(letras y numeros) no otros caracteres
print(c2.isalpha())#este metodo solo dice si hay letras
print("hola mundo".islower())#Si todo es minuscula
print("Hola Mundo".istitle())#Si sus inicios es mayusculas)
print(" - ".isspace()) #Si fuera todo son espacios
print("Hola mundo".startswith("h")) #Si la palabra comienza
print("Hola mundo".endswith('mundo'))#Si la palabra acaba 
print("Hola mundo mundo".split()) #para separar las palabras 
print("Hola mundo mundo".split()[0]) #para separar las palabras especificamente
print("Hola,mundo,mundo,otra,palabra".split(',')) #Es para separar a traves de una coma
print(",".join("Hola Mundo")) #separa caracteres
print(" ".join("Hola")) 
print("           Hola mundo   ".strip())#Para borrar los espacios
print("--------------Hola mundo---------".strip('-'))#Para borrar lo que se esta especificando
print("Hola mundo".replace('o','0'))#Cambia la palabra o la letra especificada
print("Hola mundo mundo mundo mundo mundo mundo".replace(' mundo','',3)) #Esto borra la palabra sustituyendo pero solo 3 veces lo borra

#LISTAS
lista=[1,2,3,4,5]
lista.append(6)
print(lista)
lista.clear()
print(lista)
l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)
print(["Hola","Mundo","Mundo"].count("Hola")) #Cuantos hay
print(["Hola","Mundo","Mundo"].index("Mundo")) #Esto solo busca el pirmero
l=[1,2,3]
l.insert(0,0)
print(l)
l =[5,10,15,25]
l.insert(-1,20) #Para añadir la posicion y que nmro se cambiara
print(l)
l.insert(5,30)
print(l)
l.pop(0)#Este permite borra los elementos de la lista en este caso es el primero
print(l)
l.remove(30) #Este metodo hace que borraemos algo especifico
print(l)
l=[20,30,30,30,40]
l.remove(30)
print(l)
l.reverse()#Este metodo da vuelta a la lista, este no puede revertir en cadena
print(l)
#Como revertir una lista
lista=list("Hola mundo")
print(lista)
lista.reverse()
print(lista)
cadena="".join(lista)
print(cadena)
lista=[5,-10,25,35,0,-65,100]
lista.sort() #El metodo de ordenacion
print(lista)
lista.sort(reverse=True)
print(lista)

#CONJUNTOS
c=set()
c.add(1)#agregar
c.add(2)
c.add(3)
print(c)
c.discard(1)#Permite descartar
c.add(1)
c2 =c
c2.add(4)
print(c)
c2=c.copy()
print(c2)
print(c)
c2.discard(4)
print(c2)
print(c)
c2.clear()
print(c2)
c1={1,2,3}
c2={3,4,5}
c3={-1,99}
c4={1,2,3,4,5}
print(c1.isdisjoint(c3)) #Es disjunto
print(c1.issubset(c4)) #Es un subconjunto
print(c3.issuperset(c1)) #Es un supercojunto
print(c1.union(c2)) #La union pero no lo actualiza
print(c1.union(c2)==c4) #La union de comparacion 
c1.update(c2) #Lo actualiza
print(c1)
c1={1,2,3}
c2={3,4,5}
c3={-1,99}
c4={1,2,3,4,5}
c1.difference(c2)#Este compara el conjunto diferente
print(c1.difference(c2))
c1.difference_update(c2) #Al igual que el anterior y ademas lo actualiza
print(c1)
c1={1,2,3}
c2={3,4,5}
c3={-1,99}
c4={1,2,3,4,5}
c1.intersection(c2)#El metodo de interseccion
print(c1.intersection(c2))

c1.symmetric_difference(c2) #Elementos simetricos o diferencia simetrica
print(c1.symmetric_difference(c2))

#DICCIONARIOS
colores={"amarillo":"yellow","azul":"blue","verde":"green"}
print(colores["amarillo"])
colores.get('amarillo','no se encuentra')
print(colores.get('amarillo','no se encuentra'))
print(colores.get('negro','no se encuentra'))
print('amarillo' in colores)
print(colores.keys()) #Para conseguir informacion o solamente las claves
print(colores.values())#Si se quieres sabes los valores del diccionario
print(colores.items())#Para mostrar las claves y los valores
for c in colores:
    print(colores[c])

for c in colores.keys():
    print(c)

for c in colores.items():
    print(c)
    
for c,v in colores.items():
    print(c,v)
    
colores.pop("amarillo","no se ha encontrado")#Se extraera lo especificado
print(colores)

colores.pop("negro","no se ha encontrado")#Se extraera lo especificado
print(colores.pop("negro","no se ha encontrado"))

print(colores)

colores.clear()
print(colores)


#EJERCICIOS
# 1) Utilizando otodo lo que sobre cadenas, listas, sus metodos internos... Transforma este texto:
# un dia que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondio otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
#En este otro:
#Un dia que el viento soplaba con fuerza....
#-Mira como se mueve aquella banderola -dijo el monje.
#.Lo que se mueve es el viento -respondio otro monje.
#-Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
#Lo unico prohibido es modificar directamente

texto="un dia que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondio otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lineas=texto.split("#")

for i,linea in enumerate(lineas):
    lineas[i]=linea.capitalize()
    if i==0:
        lineas[i]=lineas[i]+"..."
    else:
        lineas[i]="- "+lineas[i]+"."

for linea in lineas:
    print(linea)

#2) Crea una funcion modificar() que a partir de una lista de numeros realice las siguientes tareas sin modificar la original:
#*Borrar los elementos duplicados
#*Ordenar la lista de mayor a menor
#*Eliminar todos los numeros impares
#*Realizar una suma de todos los numeros que quedan
#*Añadir como primer elemento de la lista la suma realizada
#*Devolver la lista modificada
#*Finalmente, despues de ejecutar la funcion, comprueba que la suma de todos los numeros a partir del segundo, concuerda con el primer numero de la lista, tal que asi:

#   nueva_lista=modificar(lista)
#   print(nueva_lista[0]==sum(nueva_lista[1:5]))
#Salida de pantalla:   True
#Nota: La funcion sum(lista) devuelve una suma de los elementos de una lista

lista=[29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

def modificar(l):
    l=list(set(l))
    l.sort(reverse=True)
    for i,n in enumerate(l):
        if n%2!=0:
            del(l[i])

    suma=sum(l)
    l.insert(0,suma)
    return l

nueva_lista=modificar(lista)

print(nueva_lista)
print(lista)
print(nueva_lista[0]==sum(nueva_lista[1:5]))
        