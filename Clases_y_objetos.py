#Clases y Objetos: Introduccion
#POO: Paradigma de solucion de problemas que identifica entidades de la realidad y las traslada a clases y objetos
#Respecto a la programacion clasica:
# *Mas agil
# *Mas intuitiva
# *Mas organizable
# *Mas escalable
#TERCERA FASE
# Clases y objetos
# La herencia de clases
# Metodos de las colecciones

#Programacion estructurada vs POO
#CASO DE ESTUDIO:   Crear un registro para los clientes de una empresa con su nombre sus apellidos y su dni y el programa debe permitirnos mostrar los datos de los clientes y borrarlos a partir de su dni
print(""" Ejemplo de implementacion con Programacion Estructurada """)
clientes=[
    {'Nombre':'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111111A'},
    {'Nombre':'Juan', 'Apellidos':'Gonzales Márquez', 'dni':'2222222222B'}
]
print(clientes)
def mostrar_clientes(clientes,dni):
    for c in clientes:
        if (dni==c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return

    print("Cliente no encontrado")
mostrar_clientes(clientes,'111111111113')            
def borrar_clientes(clientes,dni):
    for i,c in enumerate(clientes):
        if (dni==c['dni']):
            del(clientes[i])
            print(str(c),"> Borrado")
            return

    print("Cliente no encontrado")

borrar_clientes(clientes,'2222222222B')       
        
print(clientes)

print("""\n\n\nEjemplo de implementacion con Programacion Orientada a Objetos no hace falta entender el codigo, lo aprenderemos en esta unidad """)
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni 
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

class Empresa:
    def __init__(self, clientes=[]):
        self.clientes=clientes
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni==dni:
                print(c)
                return
        print("Cliente no encontrado")
                
    def borrar_clientes(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni==dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")
                
hector=Cliente(nombre='Hector',apellidos='Costa Guzman',dni='111111111A')
juan=Cliente("22222222B","Juan","Gonzalo Marquez")        
Empresa=Empresa(clientes=[hector,juan])
print(hector)
print(juan)
print(Empresa.mostrar_cliente(dni="111111111A"))
print(Empresa.borrar_clientes("22222222B"))
#print(Empresa.clientes)
#POO: Se basa en determinar las entidades en lugar propio
    
#CLASES Y OBJETOS 
# La clase es como un molde para crear objetos       
class Galleta(object):
    pass

una_galleta=Galleta()
otra_galleta=Galleta()
print(type(una_galleta))
print(type(10))
print(type(3.14))
print(type("Hola"))
print(type([]))
print(type(True))
def hola():
    pass
print(type("Hola"))
print(type({}))

#ATRIBUTOS Y METODOS DE CLASE
class Galleta:
    pass

una_galleta=Galleta()
una_galleta.sabor="Salado"
una_galleta.color="Marron"
print("El sabor de esta galleta es ",una_galleta.sabor)

class Galleta:
    chocolate=False
una_galleta=Galleta()
g=Galleta
print(g.chocolate)

g.chocolate=True
print(g.chocolate)

class Galleta():
    chocolate=False
    def __init__(self):
        print("Se acaba de crear una galleta. ")
g=Galleta()

class Galleta():
    chocolate=False

    def __init__(self):
        print("Se acaba de crear una galleta. ")

    def chocolatear(self):
        self.chocolate=True


    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :)")
        else:
            print("Soy una galleta sin chocolate :(")

g=Galleta()
g.chocolatear()
g.chocolate

class Galleta():
    chocolate=False

    def __init__(self,sabor=None,forma=None):
        self.sabor =sabor
        self.forma=forma
        if sabor is not None and forma is not None:
            print("Se acaba de crear una galleta {} y {}".format(sabor,forma))

    def chocolatear(self):
        self.chocolate=True


    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :)")
        else:
            print("Soy una galleta sin chocolate :(")

g=Galleta("Salada","Cuadrada")

#METODOS ESPECIALES
class Pelicula:
    #Constructor de clase
    def __init__(self, titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Se ha creado la pelicula",self.titulo)

    #Destructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula",self.titulo)

p=Pelicula("El padrino",175,1972)
del(p)
print(str(10))
#print(str(p))
class Pelicula:
    #Constructor de clase
    def __init__(self, titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Se ha creado la pelicula",self.titulo)

    #Destructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula",self.titulo)

    #Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)
    
    def __len__(self):
        return self.duracion

p=Pelicula("El padrino",175,1972)
print(str(p)) 
print(len(p))



class Pelicula:
    #Constructor de clase
    def __init__(self, titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Se ha creado la pelicula",self.titulo)

    def __str__(self):
        return '{} ({})' .format(self.titulo,self.lanzamiento)
    
class Catalogo:
    peliculas=[]
    
    def __init__(self,peliculas=[]):
        self.peliculas=peliculas
    
    def agregar(self,p):
        self.peliculas.append(p)
        
    def mostrar(self):
        for p in self,peliculas:
            print([p])

p=Pelicula("El Padrino",175,1972)
c=Catalogo([p]) 
#c.mostrar()
c.agregar(Pelicula("El Padrino Parte 2",202,1974))
#c.mostrar()

#ENCAPSULACION DE ATRIBUTOS Y METODOS
class  Ejemplo:
    __atributo_privado="Soy un atributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde fuera")
    
e=Ejemplo()
#e.__atributo_privado
#e.__metodo_privado()

class  Ejemplo:
    __atributo_privado="Soy un atributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde fuera")
    
    def atributo_publico(self):
        return self.__atributo_privado
    
    def metodo_publico(self):
        return self.__metodo_privado()

e=Ejemplo()
print(e.atributo_publico())
print(e.metodo_publico())


#EJERCICIO
#Preparacion
#Crea una clase llamada Punto con sus coordenadas X e Y
#Añade un metodo contructor para crear puntos facilmente. Si no reciben una coordenada, su valor será cero
#Sobreescribe el metodo string, para que al imprimir por pantalla un punto aparezca en formato(X,Y)
#Añade un metodo cuadrante, que indique a que cuadrante pertenece el punto, o si es el origen
#Añade un metodo llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos
#(optativo) Añade un metodo llamado distancia, que tome otro punto y calcule la distancia ente los dos puntos y muestre por pantalla. La formula es la siguiente: 
#  d=RAIZCUADRADA((x2-x1)'2 +(y2-y1)'2)
#Nota: La funcion raiz cuadrada en phyton sqrt() se debe importar del modulo math y utilarla de la sig forma
#import math
# math.sqrt(9)

#Crea una clase llamada Rectangulo con dos puntos(inicial y final) que formaran la diagonal del rectangulo
#Añade un metodo constructor para crear ambos puntos facilmente, si no se envian se crearan dos puntos en el origen por defecto
#Añade al rectangulo un rectangulo un metodo base que muestre la base
#Añade al rectangulo un metodo altura que muestre ala altura
#Añade al rectangulo un metodo llamado area que muestre el area

#Puedes identificar facilmente estos valores si intentas dibujar el cuadrado a partir de su digonal. Si andas perdido, prueba de dibujarlo en un papel, ¡seguro que lo veras mucho mas claro! Ademas recuerda que puedes utilizar la funcion abs() para saber el valor absoluto de un numero

#EXPERIMENTACION
#Crea los puntos A(2,3), B(5,5), C(-3,-1) y D(0,0) e imprimelos por pantalla
#Consulta a que cuadrante pertenecen el punto A, C y D
#Consulta los vectores AB y BA
#(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'
#(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra mas lejos del origen, punto(0,0)
# Crea un rectangulo utilizando los puntos A y B
#Consulta la base, altura y area rectangulo. 

import math

class Punto:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "{} , {}".format(self.x,self.y)

    def cuadrante(self):
        if self.x>0 and self.y>0:
            print("{} pertenece al primer cuadrante".format
            (self))
        elif self.x<0 and self.y>0:
            print("{} pertenece al segundo cuadrante".format
            (self))
        elif self.x<0 and self.y<0:
            print("{} pertenece al tercer cuadrante".format
            (self))
        elif self.x>0 and self.y<0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self,p):
        print("El vector entre {} y {} es({}, {})".format(self,p,p.x-self.x,p.y-self.y))

    def distancia(self,p):
        d=math.sqrt((p.x-self.x)**2+(p.y-self.y)**2)
        print("La distancia entre los puntos {} y {} es {}".format(self,p,d))
        
#A(2,3), B(5,5), C(-3,-1) y D(0,0)       
A=Punto(2,3)
B=Punto(5,5)
C=Punto(-3,-1)
D=Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

class Rectangulo:
    
    def __init__(self,pInicial,pFinal):
        self.pInicial=pInicial
        self.pFinal=pFinal
        
    def base(self):
        self.base=abs(self.pFinal.x-self.pInicial.x)
        print("La base del rectangulo es {}".format(self.base))

    def altura(self):
        self.altura=abs(self.pFinal.y-self.pInicial.y)
        print("La altura del rectangulo es {}".format(self.altura))

    def area(self):
        self.base=abs(self.pFinal.x-self.pInicial.x)
        self.altura=abs(self.pFinal.y-self.pInicial.y)
        self.area=self.base*self.altura
        print("El area del rectangulo es {}".format(self.area))

R=Rectangulo(A,B)
R.base()
R.altura()
R.area()