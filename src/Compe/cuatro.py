import math
from functools import reduce

def gcd_multiple(numbers):
    return reduce(math.gcd, numbers)

# Leer número de casos
N = int(input())
casos = []

for _ in range(N):
    casos.append(tuple(map(int, input().split())))

# Procesar todos y luego mostrar los resultados
resultados = []

for a, b, c in casos:
    g = gcd_multiple([a, b, c])
    molde = a // g + b // g + c // g
    resultados.append(molde)

# Mostrar resultados
for res in resultados:
    print(res)
