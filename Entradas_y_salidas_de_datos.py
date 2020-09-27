#Entradas y salidas de datos
#Entradas: Formas de capturar datos o información desde el exterior
#Salidas: Formas de presentar los datos o información al exterior
#Leccion 01: Entradas
decimal=float(input("Introduce un numero decimal con punto: "))
valores=[]
print("Introduce 3 valores")
for x in range(3):
    valores.append(input("Introduce un valor: "))
print(valores)
#Leccion 02: Scripts
#Guiones con instrucciones en codigo fuente que se ejecutan de arriba a abajo, guardados en un fichero con un nombre unico y ejecutados desde el interprete........ Pueden tomar datos(argumentos) en el momento de la ejecucion
#Leccion se encuentra en la carpeta script
#Leccion 03: Salida
v="Otro texto"
n=10
print("Un texto ",v," y un número ",n)
c="Un texto {} y un numero {}".format(v,n)
print(c)
print("Un texto {} y un numero {}".format(v,n))
print("Un texto {1} y un numero {0}".format(v,n))
print("Un texto {texto} y un numero {numero}".format(texto=v,numero=n))
print("Un texto {v} y un numero {n}".format(v=v,n=n))
print("{v},{v},{v}".format(v=v))
print("{:>30}".format("palabra")) #Alineamiento a la derecha con 30 caracteres
print("{:<30}".format("palabra")) #Alineamiento a la izquierda con 30 caracteres
print("{:^30}".format("palabra")) #Alineamiento a la centro con 30 caracteres
print("{:.5}".format("palabra")) #Truncamiento de 3 caracteres
print("{:>30.3}".format("palabra")) #Alineamiento a la derecha con 30 caracteres con truncamiento de 3
#Formateo de numeros enteros, rellenados con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
#Formateo de numeros enteros, rellenados con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
#Formateo de numeros flotantes, rellenados con espacios
print("{:.3f}".format(3.1415926))
print("{:.3f}".format(153.21))
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))
#Formateo de numeros flotantes, rellenados con espacios
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))

#EJERCICIOS
#1. Formatea los siguientes valores para mostrar el resultado indicado:
# "Hola Mundo"--> Alineado a la derecha de 20 caracteres
# "Hola Mundo"--> Truncamiento en el cuarto carácter (indice 3)
# "Hola Mundo"--> Alineado al centro de 20 caracteres con truncamiento en el segundo caracter (indice 1)
#150 --> Formateo a 5 numeros enteros rellenados con ceros
#7887 --> Formateo a 7 numeros enteros rellenados con espacios
#20.02 --> Formateo a 3 numeros enteros y 3 numeros decimales
texto="Hola Mundo"
print("{:>20}".format(texto))
print("{:.4}".format(texto))
print("{:^20.2}".format(texto))
num1=150
num2=7887
num3=20.02
print("{:05}".format(num1))
print("{:7}".format(num2))
print("{:3.3f}".format(num3))