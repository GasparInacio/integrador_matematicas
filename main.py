from ejercicios import extraer_digitos_unicos, interseccion, union, diferencia, diferencia_simetrica, frecuencia_dnis, \
    sumar_digitos, diversidad_numerica, digitos_compartidos, es_par, grupo_z, es_bisiesto, producto_cartesiano

# Operación con DNIs
# DNIs de integrantes del grupo
dni1 = 37050296
dni2 = 37860214

# Formación de los conjuntos con digitos únicos de cada integrante
conjunto1 = extraer_digitos_unicos(dni1)
conjunto2 = extraer_digitos_unicos(dni2)
#print('DNI1: ', dni1)
#print('DNI2: ', dni2)
#print('Conjunto 1: ', conjunto1)
#print('Conjunto 2: ', conjunto2)

# Operación para la unión de los conjuntos
#print('Unión de los conjuntos: ', union(conjunto1, conjunto2))
# La unión de los conjuntos es la cantidad de elementos únicos
#print('La unión se representa como la suma de todos los elementos del diagrama')

# Operación para la intersección de los conjuntos
#print('Elementos que están en los dos conjuntos: ', interseccion(conjunto1, conjunto2))

# Operaciónpara la diferencia de los conjuntos
# La diferencia entre dos conjuntos hace referencia a los elementos que están en uno pero no en el otro.
# Diferencia entre a y b
#print('Interseccion entre conjunto1 y conjunto2: ', diferencia(conjunto1, conjunto2))
#print('Elementos que estan en conjunto1 pero no en conjunto2')
#print('Interseccion entre conjunto2 y conjunto1: ', diferencia(conjunto2, conjunto1))
#print('Elementos que estan en conjunto2 pero no en conjunto1')

# Operación para diferencia simétrica de los conjuntos
# La diferencia simétrica son los elementos que están en A o en B, pero no en ambos.
#diferencia_simetrica(conjunto1, conjunto2)
#print('Elementos que están en conjunto1 o en conjunto2 pero no en los dos')

# Conteo de frecuencias de cada dígito
#print('Frecuencia de los números en los DNIs: ', frecuencia_dnis(dni1, dni2))

# Sumar digitos de los DNIs
#print('La suma de los dígitos del DNI1 es: ', sumar_digitos(dni1))
#print('La suma de los dígitos del DNI1 es: ', sumar_digitos(dni2))

# Evaluaciones lógicas
# Diversidad numérica
#diversidad_numerica(conjunto1, conjunto2)
# Dígitos compartidos
#digitos_compartidos(conjunto1, conjunto2)

# Operación con años de nacimiento
# variables con años de nacimientos
anio1 = 1993
anio2 = 1998

# Nacimiento en años pares o impares
#es_par(anio1, anio2)

# Grupo Z
#grupo_z(anio1, anio2)

# Año especial
#if es_bisiesto(anio1) or es_bisiesto(anio2):
#    print('Tenemos un año especial')
#else:
#    print('Ninguno nació en un año especial')

# Producto cartesiano entre conjunto de años y conjunto de edades
#print(producto_cartesiano(anio1, anio2))