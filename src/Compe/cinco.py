import sys

# Precalcular cantidad de divisores hasta 100000
MAX = 100000
divisores = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        divisores[j] += 1

# Generar la secuencia NuNuDoN
nunudon = [1]
while True:
    ultimo = nunudon[-1]
    siguiente = ultimo + divisores[ultimo]
    if siguiente > MAX:
        break
    nunudon.append(siguiente)

# Leer toda la entrada primero
N = int(input())
casos = []

for _ in range(N):
    A, B = map(int, input().split())
    casos.append((A, B))

# Procesar los casos y almacenar las respuestas
respuestas = []

for A, B in casos:
    # Contar cuántos elementos están dentro del rango [A, B]
    cuenta = sum(1 for x in nunudon if A <= x <= B)
    respuestas.append(cuenta)

# Mostrar resultados uno por uno
for r in respuestas:
    print(r)
