#Falta de aqui en adelante
#def saludar():
#    print("Hola, te estoy saludando desde la funcion saludar del modulo saludos")

from collections import Counter
l=[1,2,3,4,1,2,3,2,1]
print(Counter(l))   
p="palabra"
print(Counter(p))
animales="gato perro canario perro canario perro"
print(Counter(animales))
print(animales.split())
print(Counter(animales.split()))
c=Counter(animales.split())
print(c.most_common(1))
print(c.most_common(2))
print(c.most_common())
I=[10,20,30,40,10,20,30,10,20,10]
x=Counter(I)
print(x.items())
print(x.keys())
print(x.values())
print(sum(x.values()))
print(list(x))
d=list(x)
#print(d.most_common(1))
print(set(x))   
d=['Algo']
from collections import defaultdict
d=defaultdict(float)
print(d['algo'])
print(d)
d=defaultdict(str)
print(d['algo'])
print(d)
d=defaultdict(object)
print(d['algo'])
print(d)
d['algo']=19.5
print(d['algo'])
d['algomas']=0
print(d)
n={}
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)

from collections import OrderedDict
n=OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)

n1={}
n1['uno'] = 'one'
n1['dos'] = 'two'

n2={}
n2['uno'] = 'one'
n2['dos'] = 'two'

print(n1==n2)

n1=OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'

n2=OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'

print(n1==n2)

t=(20,40,60)
print(t[0])
print(t[-1])

from collections import namedtuple
Persona=namedtuple('Persona','nombre apellido edad')
p=Persona(nombre="Eddie",apellido="Huaripayta",edad=22)
print(p.nombre)
print(p.apellido)
print(p[0])
print(p)


import datetime
dt=datetime.datetime.now()#Ahora
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.tzinfo)#Es la zona horario pero no esta establecida
print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("{}/{}/{}".format(dt.day,dt.month,dt.year))
dt=datetime.datetime(2020,1,1)
print(dt) 
dt=dt.replace(year=3000)
print(dt)
dt=datetime.datetime.now()#Ahora
print(dt.isoformat())
print(dt.strftime("%A %d %B %Y %I:%M"))
import locale
print(locale.setlocale(locale.LC_ALL,'es'))
print(dt.strftime("%A %d %B %Y %I:%M"))
print(locale.setlocale(locale.LC_ALL,'zh-CN'))
print(dt.strftime("%A %d %B %Y %I:%M"))
print(locale.setlocale(locale.LC_ALL,'es-ES'))
print(dt.strftime("%A %d %B %Y - %I:%M"))
dt=datetime.datetime.now()
print(dt)
t=datetime.timedelta(days=14, seconds=1000, hours=4)
dentro_de_dos_semanas=dt+t
print(dentro_de_dos_semanas)
print(dentro_de_dos_semanas.strftime("%A %d %B %Y - %I:%M"))
hace_dos_semanas=dt-t
print(hace_dos_semanas)

#import pytz#Falta instalar el pyp3 con eso 
#print(pytz.all_timezones)

import math
pi=3.14159
print(round(pi))#Redondeo
print(math.floor(pi))
print(math.ceil(pi))
print(abs(-19))
n=[1,2,3]
print(sum(n))
print(math.fsum(n))
n=[0.99999999999,1,2,3]
print(sum(n))
print(math.fsum(n))
print(math.trunc(200.4399847))
print(2**3)
print(math.pow(2,3))
print(math.sqrt(8))
#math.pi()#No me funciona
# print(math.e())

import random
print(random.random()) #>=0y <1.0
print(random.random()) #>=0y <1.0
print(random.random()) #>=0y <1.0
print(random.random()) #>=0y <1.0
print(random.uniform(1, 10)) #>=1y <10
print(random.uniform(1, 10)) #>=1y <10
print(random.randrange(10)) #>=0 y <10
print(random.randrange(10)) #>=0 y <10
print(random.randrange(10)) #>=0 y <10
print(random.randrange(10)) #>=0 y <10
print(random.randrange(0,101,2)) #>=0 y <100 con multiplos de 2
print(random.randrange(0,101,5)) #>=0 y <100 con multiplos de 5
c="Hola mundo"
print(random.choice(c))
l=[1,2,3,4,5,6]
print(random.choice(l))
random.shuffle(l)
print(l)
print(random.sample(l,3))