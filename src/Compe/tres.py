import math

# Preprocesar los primos con la criba hasta el máximo n posible
MAX_N = 100000
es_primo = [True] * (MAX_N + 1)
es_primo[0] = es_primo[1] = False

for i in range(2, int(MAX_N ** 0.5) + 1):
    if es_primo[i]:
        for j in range(i * i, MAX_N + 1, i):
            es_primo[j] = False

# Crear un arreglo con P(n) = cantidad de primos ≤ n
P = [0] * (MAX_N + 1)
contador = 0
for i in range(MAX_N + 1):
    if es_primo[i]:
        contador += 1
    P[i] = contador

# Leer entradas
C = int(input())
valores = []

for _ in range(C):
    n = int(input())
    valores.append(n)

# Calcular y mostrar resultados
for n in valores:
    estimacion = n / math.log(n)
    error = round(P[n] - estimacion)
    print(error)
