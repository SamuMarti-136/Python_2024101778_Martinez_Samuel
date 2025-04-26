'''
Ejercicios
'''

#Pedir al usuario que ingrese dos numeros
n1= int(input("Ingrese un numero:"))
n2= int(input("Ingrese otro numero:"))

#Verificar si los numeros son pares
par1=n1 % 2 == 0
par2=n2 % 2 == 0

#Mostrar los resultados
if par1 and par2:
    print("Ambos numeros son pares.")
elif par1:
    print("Solo el primer numero es par.")
elif par2:
    print("Solo el segundo numero es par")
else:
    print("Ninguno de los numeros son pares.")