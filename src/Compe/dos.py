import math
from functools import reduce

# Función para calcular el MCM de dos números
def mcm(a, b):
    return a * b // math.gcd(a, b)

# Función para calcular el MCM de una lista de números
def mcm_lista(numeros):
    return reduce(mcm, numeros)

# Leer número de casos
N = int(input())
casos = []

# Leer todos los casos
for _ in range(N):
    line = list(map(int, input().split()))
    casos.append(line)

# Procesar y mostrar resultados
for caso in casos:
    print(mcm_lista(caso))
