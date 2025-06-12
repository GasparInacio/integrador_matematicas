import matplotlib.pyplot as plt
from matplotlib_venn import venn2


# Función para generar diagramas de venn con la librería matplotlib
def mostrar_diagrama_venn_2(a, b):
    venn2((a, b), set_labels=("DNI1", "DNI2"))
    plt.title("Diagrama de Venn\nmuestra la cantidad de números que se encuentran en cada parte")
    plt.show()


# Operaciones con DNIs
def extraer_digitos_unicos(dni):
    return set(str(dni))


def union(a, b):
    mostrar_diagrama_venn_2(a, b)
    union_conjuntos = a.union(b)
    return union_conjuntos


def interseccion(a, b):
    mostrar_diagrama_venn_2(a, b)
    intersection_conjuntos = a.intersection(b)
    return intersection_conjuntos


def diferencia(a, b):
    mostrar_diagrama_venn_2(a, b)
    diferencia_conjuntos = a.difference(b)
    return diferencia_conjuntos


def diferencia_simetrica(a, b):
    mostrar_diagrama_venn_2(a, b)
    dif_simetrica = a.symmetric_difference(b)
    return dif_simetrica


def frecuencia_dnis(a, b):
    digitos = list(str(a) + str(b))
    frecuencia = {}
    for digito in digitos:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    return frecuencia


def sumar_digitos(a):
    numeros = list(str(a))
    suma = 0
    for digito in numeros:
        suma += int(digito)
    return suma


# Operaciones lógicas
def diversidad_numerica(a, b):
    conj1 = list(str(a))
    conj2 = list(str(b))
    if len(conj1) or len(conj2) >= 6:
        print('Diversidad numérica alta')
    else:
        print('No existe diversidad numérica alta en ningún conjunto')


def digitos_compartidos(a, b):
    compartidos = a.intersection(b)
    if compartidos:
        print('Dígitos compartidos: ', compartidos)
    else:
        print('No se comparten dígitos entre los conjuntos')


# Operaciones con años
def es_par(a, b):
    par = 0
    impar = 0
    anios = [a, b]
    for anio in anios:
        if anio % 2 == 0:
            par += 1
        else:
            impar += 1
    print('Nacieron en años pares: ', par)
    print('Nacieron en años impares: ', impar)


def grupo_z(a, b):
    if (a and b) > 2000:
        print('Grupo Z')
    elif (a or b) > 2000:
        print('Uno de los integrantes pertenece al Grupo Z')
    else:
        print('Ninguno de los integrantes pertenece al Grupo Z')


def es_bisiesto(a):
    return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)


def producto_cartesiano(a1, a2):
    anios = [a1, a2]
    edades = [2025 - i for i in anios]
    return [(a, e) for a in anios for e in edades]