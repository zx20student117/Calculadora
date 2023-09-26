"""
Calculadora en python
"""

num_1 = int(input("Ingrese el primer numero: "))

num_2 = int(input("Ingrese el segundo numero: "))

def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

resultado_1 = sumar(num_1, num_2)

resultado_2 = restar(num_1, num_2)

print("El resultado es: ", resultado_1)

print("El resultado es: ", resultado_2)