#1. Realiza un programa que lea 2 numeros por teclado y determine los siguientes aspectos (es suficiente mostrar true o false)
a=1
b=1
print(a==b)
c=2
d=4
print(c==d)
if a>b:
    print("Es real")
elif b<c:
    print("Es lo elegido")
else:
    print("Es la otra opción")

#2. Utilizando operadores logicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10(es suficiente con mostrar True o False)
cadena = input("Escribe una cadena: ")
condiciones=len(cadena)>=3 and len(cadena) < 10
print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10? ",condiciones) #Me mostrará si es true o false
#3. Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
# . Guarda en una variable numero_magico el valor 1234679(sin el 8)
# .Lee por pantalla otro numero_usuario especifica que sea entre 1 y 9 (asegurate que es un numero)
# .Multiplica el numero_usuario por 9 en si mismo
# . Multiplica el numero_magico por numero_usuario en si mismo
# . Finalmente muestra el valor final del numero_magico por pantalla
numero_magico=12345679
numero_usuario= int(input("Introduce un numero del 1 al 9: "))
numero_usuario*=9
numero_magico*=numero_usuario
print("El numero magico es: ", numero_magico)
