from ejercicios import extraer_digitos_unicos, interseccion, union, diferencia, diferencia_simetrica, frecuencia_dnis, \
    sumar_digitos, diversidad_numerica, digitos_compartidos, es_par, grupo_z, es_bisiesto, producto_cartesiano, \
    mostrar_diagrama_venn_2

# Archivo para recopilar y modularizar los ejercicios y submenús


# funciones para ejercicios


# Ejercicios con DNIs
# Datos
# DNIs de integrantes del grupo
dni1 = 37050296
dni2 = 38987027

# Formación de los conjuntos con digitos únicos de cada integrante
conjunto1 = extraer_digitos_unicos(dni1)
conjunto2 = extraer_digitos_unicos(dni2)


def imprimir_datos():
    print('\nDNI1: ', dni1)
    print('DNI2: ', dni2)
    print('Conjunto 1: ', conjunto1)
    print('Conjunto 2: ', conjunto2)


def union_conjuntos():
    # Operación para la unión de los conjuntos
    print('\nUnión de los conjuntos: ', union(conjunto1, conjunto2))
    # La unión de los conjuntos es la cantidad de elementos únicos


def interseccion_conjuntos():
    # Operación para la intersección de los conjuntos
    print('\nElementos que están en los dos conjuntos (intersección): ', interseccion(conjunto1, conjunto2))


def diferencia_conjuntos():
    # Operaciónpara la diferencia de los conjuntos
    # La diferencia entre dos conjuntos hace referencia a los elementos que están en uno pero no en el otro.
    # Diferencia entre a y b
    print('\nElementos que estan en conjunto1 pero no en conjunto2')
    print(diferencia(conjunto1, conjunto2))
    print('Elementos que estan en conjunto2 pero no en conjunto1')
    print(diferencia(conjunto2, conjunto1))


def dif_simetrica_conjuntos():
    # Operación para diferencia simétrica de los conjuntos
    # La diferencia simétrica son los elementos que están en A o en B, pero no en ambos.
    print('\nElementos que están en conjunto1 o en conjunto2 pero no en los dos')
    print(diferencia_simetrica(conjunto1, conjunto2))


def frecuencia_digitos():
    # Conteo de frecuencias de cada dígito
    print('\nFrecuencia de los números en los DNIs: ', frecuencia_dnis(dni1, dni2))


def suma_digitos_dni():
    print('\nLa suma de los dígitos del DNI1 es: ', sumar_digitos(dni1))
    print('La suma de los dígitos del DNI2 es: ', sumar_digitos(dni2))


def evaluacion_logica():
    # Evaluaciones lógicas
    # Diversidad numérica
    diversidad_numerica(conjunto1, conjunto2)
    # Dígitos compartidos
    digitos_compartidos(conjunto1, conjunto2)


# Sybmenú DNIs
def submenu_dnis():
    while True:
        print('\n#############################################')
        print('Operaciones con DNIs')
        print('#############################################')
        print(
            '\n1. Operaciones con conjuntos\n2. Conteo de frecuencia de los dígitos\n3. suma de dígitos de cada DNI\n4. Evaluación de condiciones lógicas\n5. Imprimir diagrama de Venn')

        try:
            opc_dnis = int(input('\nIngrese una opción ó "0" para salir: '))
        except ValueError:
            print('\nOpcion incorrecta, intente nuevamente')
            continue

        if opc_dnis == 0:
            break
        elif opc_dnis == 1:
            imprimir_datos()
            union_conjuntos()
            interseccion_conjuntos()
            diferencia_conjuntos()
            dif_simetrica_conjuntos()
            continue
        elif opc_dnis == 2:
            imprimir_datos()
            frecuencia_digitos()
            continue
        elif opc_dnis == 3:
            imprimir_datos()
            suma_digitos_dni()
            continue
        elif opc_dnis == 4:
            imprimir_datos()
            evaluacion_logica()
            continue
        elif opc_dnis == 5:
            mostrar_diagrama_venn_2(conjunto1, conjunto2)
            continue
        else:
            print('\nOpcion incorrecta, intente nuevamente')
            continue


# Ejercicios con años
# Datos
anio1 = 1993
anio2 = 1995


def imprimir_datos_anio():
    print('\nAños:')
    print(anio1)
    print(anio2)


def par_impar():
    # Nacimiento en años pares o impares
    es_par(anio1, anio2)


def grupo_z_anio():
    # Grupo Z
    grupo_z(anio1, anio2)


def bisiesto():
    # Año especial
    if es_bisiesto(anio1) or es_bisiesto(anio2):
        print('\nTenemos un año especial')
    else:
        print('\nNinguno nació en un año especial')


def prod_cartesiano_anio():
    # Producto cartesiano entre conjunto de años y conjunto de edades
    print('\n', producto_cartesiano(anio1, anio2))


# Submenú años
def submenu_anios():
    while True:
        print('\n#############################################')
        print('Operaciones con DNIs')
        print('#############################################')
        print(
            '\n1. Años pares o impares\n2. Grupo Z\n3. Años bisiestos\n4. Producto cartesiano entre conjunto de años y conjunto de edades')

        try:
            opc_anios = int(input('Ingrese una opción ó "0" para salir: '))
        except ValueError:
            print('\nOpcion incorrecta, intente nuevamente')
            continue

        if opc_anios == 0:
            break
        elif opc_anios == 1:
            imprimir_datos_anio()
            par_impar()
            continue
        elif opc_anios == 2:
            imprimir_datos_anio()
            grupo_z_anio()
            continue
        elif opc_anios == 3:
            imprimir_datos_anio()
            bisiesto()
            continue
        elif opc_anios == 4:
            imprimir_datos_anio()
            prod_cartesiano_anio()
            continue
        else:
            print('\nOpcion incorrecta, intente nuevamente')
            continue
