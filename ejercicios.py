import matplotlib.pyplot as plt
from matplotlib_venn import venn2


# Función para generar diagramas de venn con la librería matplotlib
def mostrar_diagrama_venn_2(a, b):
    venn2((a, b), set_labels=("DNI1", "DNI2"))
    plt.title("Muestra la cantidad de números que\nse encuentran en cada parte del diagrama")
    plt.show()


# Operaciones con DNIs
def extraer_digitos_unicos(dni):
    return {int(digito) for digito in str(dni)}


# Operaciones con conjuntos
def union(a, b):
    return a.union(b)


def interseccion(a, b):
    return a.intersection(b)


def diferencia(a, b):
    return a.difference(b)


def diferencia_simetrica(a, b):
    return a.symmetric_difference(b)


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
    if (len(a) and len(b)) >= 5:
        print('\nDiversidad numérica alta')
    else:
        print('\nNo existe diversidad numérica alta en los conjunto')


def digitos_compartidos(a, b):
    compartidos = a.intersection(b)
    if compartidos:
        print('\nDígitos compartidos: ', compartidos)
    else:
        print('\nNo se comparten dígitos entre los conjuntos')


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
    print('\nNacieron en años pares: ', par)
    print('Nacieron en años impares: ', impar)


def grupo_z(a, b):
    if (a and b) > 2000:
        print('Grupo Z')
    elif (a or b) > 2000:
        print('\nUno de los integrantes pertenece al Grupo Z')
    else:
        print('\nNinguno de los integrantes pertenece al Grupo Z')


def es_bisiesto(a):
    return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)


def producto_cartesiano(a1, a2):
    anios = [a1, a2]
    edades = [2025 - i for i in anios]
    return [(a, e) for a in anios for e in edades]
