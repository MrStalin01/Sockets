import random
def matriz(mostrarmatriz):
    for fila in mostrarmatriz:
        print(fila)


def es_cuadrado_magico(matriz):
    if not matriz:
        return False

    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False

    suma_magica = sum(matriz[0])
    for fila in matriz:
        if sum(fila) != suma_magica:
            return False

    for j in range(n):
        suma_columna = 0
        for i in range(n):
            suma_columna += matriz[i][j]
        if suma_columna != suma_magica:
            return False

    suma_diagonal_p = 0
    for i in range(n):
        suma_diagonal_p += matriz[i][i]
    if suma_diagonal_p != suma_magica:
        return False

    suma_diagonal_s = 0
    for i in range(n):
        suma_diagonal_s += matriz[i][n - 1 - i]
    if suma_diagonal_s != suma_magica:
        return False

    return True

tabla = []

for x in range(4):
    tabla.append([])
    for y in range(4):
        tabla[x].append(random.randint(0, 9))

print("--- Matriz Generada ---")
matriz(tabla)

print("\n--- Verificación de Cuadrado Mágico ---")
if es_cuadrado_magico(tabla):
    suma_m = sum(tabla[0])
    print(f"La matriz es un CUADRADO MÁGICO! (Suma Mágica: {suma_m})")
else:
    print("La matriz NO es un cuadrado mágico.")