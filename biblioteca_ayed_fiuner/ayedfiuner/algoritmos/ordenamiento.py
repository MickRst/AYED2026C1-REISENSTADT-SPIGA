"""
ordenamiento.py
Implementación de tres algoritmos de ordenamiento:
  - Burbuja   O(n²)
  - Quicksort O(n log n) promedio
  - Radix Sort O(n·k)
"""


def burbuja(lista):
    """
    Ordenamiento burbuja.
    Precondición: lista es una lista de números.
    Postcondición: devuelve una nueva lista ordenada de menor a mayor.
    Complejidad: O(n²) en caso promedio y peor caso.

    Idea: recorre la lista comparando pares adyacentes y los intercambia
    si están en el orden incorrecto. Cada pasada "burbujea" el mayor
    elemento hacia el final. Se repite n-1 veces.
    """
    resultado = lista[:]          # copia para no modificar la original
    n = len(resultado)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    return resultado


def quicksort(lista):
    """
    Ordenamiento quicksort (recursivo).
    Precondición: lista es una lista de números.
    Postcondición: devuelve una nueva lista ordenada de menor a mayor.
    Complejidad: O(n log n) caso promedio, O(n²) peor caso (lista ya ordenada).

    Idea: elige un pivote (elemento del medio), separa los elementos en
    menores, iguales y mayores al pivote, y aplica quicksort recursivamente
    a los dos subgrupos extremos.
    """
    if len(lista) <= 1:
        return lista[:]

    pivote = lista[len(lista) // 2]
    menores  = [x for x in lista if x < pivote]
    iguales  = [x for x in lista if x == pivote]
    mayores  = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)


def radix_sort(lista):
    """
    Ordenamiento por residuos (Radix Sort, base 10).
    Precondición: lista es una lista de enteros no negativos.
    Postcondición: devuelve una nueva lista ordenada de menor a mayor.
    Complejidad: O(n·k) donde k es la cantidad de dígitos del número mayor.

    Idea: ordena los números dígito por dígito, empezando por el menos
    significativo (unidades), luego decenas, centenas, etc.
    Usa counting sort estable en cada pasada.
    """
    if not lista:
        return []

    resultado = lista[:]
    maximo = max(resultado)

    # Procesa cada posición de dígito (1, 10, 100, ...)
    exp = 1
    while maximo // exp > 0:
        resultado = _counting_sort_por_digito(resultado, exp)
        exp *= 10

    return resultado


def _counting_sort_por_digito(lista, exp):
    """
    Counting sort estable auxiliar para radix sort.
    Ordena por el dígito en la posición 'exp' (1=unidades, 10=decenas...).
    Complejidad: O(n).
    """
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10          # dígitos del 0 al 9

    # Cuenta ocurrencias de cada dígito
    for num in lista:
        digito = (num // exp) % 10
        conteo[digito] += 1

    # Acumula: conteo[i] ahora dice cuántos elementos van ANTES de i
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construye la salida recorriendo de atrás hacia adelante (estabilidad)
    for i in range(n - 1, -1, -1):
        digito = (lista[i] // exp) % 10
        conteo[digito] -= 1
        salida[conteo[digito]] = lista[i]

    return salida
