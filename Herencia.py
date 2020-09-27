#Herencia 
# Capacidad de una clase de heredar atributos y metodos de otra, además de agregar de nuevos o modificar los heredados
# clases madres y clases hijas que en el mundo de la programacion Clase y Subclase

#Herencia
class Producto:
    def __init__(self, referencia,tipo,nombre,pvp,descripcion,productor=None,distribuidor=None,isbn=None,autor=None):
        self.referencia=referencia
        self.tipo=tipo
        self.nombre=nombre
        self.pvp=pvp
        self.descripcion=descripcion
        self.productor=productor
        self.distribuidor=distribuidor
        self.isbn=isbn
        self.autor=autor

adorno=Producto('000A','ADORNO','Vaso Adornado',15,'Vaso de porcelana con dibujos')
print(adorno)
print(adorno.tipo)

class Producto:
    def __init__(self, referencia,nombre,pvp,descripcion):
        self.referencia=referencia
        self.nombre=nombre
        self.pvp=pvp
        self.descripcion=descripcion
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)
 
class Adorno(Producto):
    pass

ad=Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")
print(ad)

class Alimento(Producto):
    productor=""
    distribuidor=""

def __str__(self):
        return """\ 
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t\{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

al=Alimento(2035,"Botella de Aceite de Oliva Extra",5,"250 ML")
al.productor="La Aceitera"
al.distribuidor="Distribuciones SA"
print(al)

class Libro(Producto):
    isbn=""
    autor=""

def __str__(self):
        return """\ 
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\t{}
AUTOR\t\{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)

li=Libro(2036,"Cocina Mediterranea",9,"Recetas sanas y buenas")
li.isbn="0-123456-78-9"
li.autor="Doña Juana"
print(li)

#CLASES HEREDADAS Y POLIMORFISMO
#POLIMORFIA: Propiedad de la herencia en que objetos de distintas subcclases pueden responder una misma accion
#El caso nuestro, el metodo rebajar_producto() recibe objetos de distintas clases y accede al atributo pvp dando por hecho que existe en ellos

ad=Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")

al=Alimento(2035,"Botella de Aceite de Oliva Extra",5,"250 ML")
al.productor="La Aceitera"
al.distribuidor="Distribuciones SA"

li=Libro(2036,"Cocina Mediterranea",9,"Recetas sanas y buenas")
li.isbn="0-123456-78-9"
li.autor="Doña Juana"

productos=[ad,al]
productos.append(li)
print(productos)

for p in productos:
    print(p,"\n")

for p in productos:
    print(p.referencia,p.nombre)

#for p in productos:
#    print(p.autor) #Error porque no esta en la subclase

for p in productos:
    if ( isinstance(p, Adorno) ):
        print("\n",p.referencia,p.nombre)

    elif ( isinstance(p, Alimento) ):
        print(p.referencia,p.nombre,p.productor)

    elif ( isinstance(p, Libro) ):
        print(p.referencia,p.nombre,p.isbn)

def rebajar_producto(p,rebaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio"""
    p.pvp=p.pvp-(p.pvp/100*rebaja)
    return p

al_rebajado=rebajar_producto(al,10)
print("\n",al_rebajado)
print("\n",al)

copia_al=al
copia_al.referencia=2038
print("\n",copia_al)

l=[1,2,3]
l2=l
l2.append(4)
print("\n",l)

import copy
#El copy funciona con cualquier clase 
copia_ad=copy.copy(ad)
print("\n",copia_ad)

copia_ad.pvp=25
print("\n",copia_ad,"\n") 

#El caso nuestro, el metodo rebajar_producto() recibe objetos de distintas clases y accede al atributo pvp dando por hecho que existe en ellos
#En Python todas las clases son a su vez subclases de la superclase Object, es decir, son polimorficas por defecto
 
#HERENCIA MULTIPLE
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este metodo lo heredo de A")


class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este metodo lo heredo de B")
        
class C(B,A): #En este juego de parentesis hay una jerarquia por la izquierda
    def c(self):
        print("Este metodo es de C")

c=C()
c.a()
c.b()
c.c()


#Ejercicio
class Vehiculo():
    
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):
    
    def __init__(self,color,ruedas,velocidad,cilindrada):
        self.color=color
        self.ruedas=ruedas
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc".format(self.color,self.velocidad,self.ruedas,self.cilindrada)
    
c=Coche("Azul",4,150,1200)
print(c)

#El incoveniente mas evidente de ir sobreescribiendo es que tenemos que volver a escribir el codigo de la superclase y luego el especifico de la superclase

class Vehiculo():
    
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):
    
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas) #Utilizamos super() sin self en lugar de vehiculo
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return super().__str__()+", {} km/h, {} cc".format(self.velocidad,self.cilindrada)

c=Coche("Azul",4,150,1200)
print(c)

#EXPERIMENTA
#Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos
#Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos
#Modifica la funcion catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre unicamente los que su numero de ruedas concuerde con el valor del argumento. Tambien debe mostrar un mensaje "Se han encontrado {} vehiculos con {} ruedas." unicamente si se envia el argumento ruedas. Ponla a prueba con 0,2 y 4 ruedas como valor
#Recordatorio. Puedes utilizar el atributo especial de clase name de la siguiente forma para recuperar el nombre de la clase de un objeto.
# type(objeto).__name__
 
class Coche(Vehiculo):
    
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas) #Utilizamos super() sin self en lugar de vehiculo
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return super().__str__()+", {} km/h, {} cc".format(self.velocidad,self.cilindrada)

class Camioneta(Coche):

    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada) #Utilizamos super() sin self en lugar de vehiculo
        self.carga=carga

    def __str__(self):
        return super().__str__()+", {} kg de carga".format(self.carga)

class Bicicleta(Vehiculo):
    
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas) #Utilizamos super() sin self en lugar de vehiculo
        self.tipo=tipo
        
    def __str__(self):
        return super().__str__()+", {}".format(self.tipo)

class Motocicleta(Bicicleta):
    
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo) #Utilizamos super() sin self en lugar de vehiculo
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def __str__(self):
        return super().__str__()+", {} km/h, {} cc".format(self.velocidad,self.cilindrada)


Vehiculo=[
    Coche("Azul",4,150,1200),
    Camioneta("Blanco",4,100,1300,1500),
    Bicicleta("Verde",2,"Urbana"),
    Motocicleta("Negro",2,"Deportiva",180,900)
]

#def Catalogar(lista):
#    for v in lista:
#        print("\n{} {}".format(type(v).__name__, v))

#Catalogar(Vehiculo)


def Catalogar(lista,ruedas=None):

    if ruedas!=None: #Estoes un buscador o un filtrador
        contador=0
        for v in Vehiculo:
            if v.ruedas==ruedas:
                   contador+=1
        print("Se han encontrado {} vehiculos con {} ruedas.".format(contador,ruedas))
        print("======================================")

    for v in lista: #esto mostrara lo q se esta buscando
        if ruedas==None:
            print("\n{} {}".format(type(v).__name__, v))
        else:
            if v.ruedas==ruedas:
               print("\n{} {}".format(type(v).__name__, v)) 

Catalogar(Vehiculo, 0)
