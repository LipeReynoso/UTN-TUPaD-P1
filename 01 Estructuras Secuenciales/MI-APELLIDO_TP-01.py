'''/Reynoso Felipe Andres TP1 de programacion 1'''
'''Aclaracion: quita las comillas correspondiente para ejecutar el programa'''

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

'''print ("hola, mundo")'''

# 2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

'''
nombre = input ("Por favor ingrese su nombre")
print("!hola",nombre, "!Es un gusto poder conocerte!")
'''

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

'''
nombre = input ("Por favor ingrese su nombre")
apellido = input ("Por favor ingresa tu apellido")
edad = input ("Por favor Ingrese su edad")
pais = input ("Por favor ingresa el pais donde vives")
print("Hola mi nombre es",nombre,apellido, "tengo", edad, "años y soy de", pais,)
'''

# 4)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

'''
import math

Solicita el valor del radio al usuario
radio = float(input("Por favor, ingresa el valor del radio del círculo: "))

#Calcula el área y el perímetro
area = math.pi * radio**2
perimetro = 2 * math.pi * radio

# Muestra los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
'''

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

'''
segundos=float(input("Ingrese la cantidad de segundos: "))
hora=int(60)
horas=(segundos/hora)
print( segundos,"segundos es equivalente a: ",horas,"horas" )
'''

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

'''
numero=int(input("ingrese un numero: "))

vamos a generar la tabla de multiplicar hasta 10
for i in range(1,11):
    #resultado= numero *i
    #print (f"{numero} x {i} = {resultado}")
'''

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

''' numero1=int(input("ingrese un primer numero distinto de 0: "))
if numero1 != 0:
    print("numero ingresado correctamente")
else:
    print("A ingresado un 0 como valor")
numero2=int(input("ingrese un segundo numero distinto de 0: "))
if numero2 != 0:
    print("numero ingresado correctamente")
else:
    print("A ingresado un 0 como valor")

#Multiplicacion
multi= numero1 * numero2
print(f"{numero1} * {numero2} = {multi}")

#Suma
suma= numero1 + numero2
print (f"{numero1} + {numero2} = {suma}")

#Resta
resta= numero1 - numero2
print(f"{numero1} - {numero2} = {resta}")

#Division
div= numero1 / numero2
print(f"{numero1} / {numero2} = {div}") '''


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: IMC: pesos en kg/(altura en mts)**2

'''altura=float(input("ingrese su altura en mts: "))
peso=float(input("Ingrese su peso en kilos:"))

# Calcular el IMC
imc=peso/ (altura**2)
print(f"El imc es de: {imc}")'''

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

'''
temp_celsius=float(input("ingrese la temperatura: "))

# Calculamos la equivalencia
temp_fah= ((9/5) * temp_celsius) + 32
print(f"la temperatura en Celsius es de {temp_celsius} cuyo equivalente en Fahrenheit es de {temp_fah}")
'''

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

'''
num1=float(input("Ingrese un primer numero: "))
num2=float(input("Ingrese un segundo numero: "))
num3=float(input("Ingrese un tercer numero: "))

#calculamos el promedio de los numeros ingresados
sum_prom=num1+num2+num3
prom= (sum_prom/3)
#mostramos el resultado por pantalla
print(f"el promedio de los numeros ingresados es de: {prom}")
'''