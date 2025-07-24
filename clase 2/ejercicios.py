'''
crear un programa que pida dos numeros
y obtgenga cual de ellos es par
o si ambos lo son
# si ambos son pares, mostrar un mensaje" ambos son pares
# si uno es par y otro impar, mostrar un mensaje "uno es par y otro impar"
'''
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

es_par1 = numero1 % 2 == 0
es_par2 = numero2 % 2 == 0
if es_par1 and es_par2:
    print("Ambos números son pares")
elif (es_par1 and not es_par2) or (not es_par1 and es_par2):
    print("Uno es par y otro impar")
else:
    print("Ambos números son impares")
    