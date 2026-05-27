def _counting_sort_por_digito(lista, exp):
    """Counting sort estable auxiliar para radix sort."""
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10
    for num in lista:
        digito = (num // exp) % 10
        conteo[digito] += 1
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    for i in range(n - 1, -1, -1):
        digito = (lista[i] // exp) % 10
        conteo[digito] -= 1
        salida[conteo[digito]] = lista[i]
    return salida


def radix_sort(lista):
    """
    Ordenamiento por residuos (Radix Sort, base 10).
    Precondición: lista es una lista de enteros no negativos.
    Postcondición: devuelve una nueva lista ordenada de menor a mayor.
    Complejidad: O(n·k) donde k es la cantidad de dígitos del número mayor.
    """
    if not lista:
        return []
    resultado = lista[:]
    maximo = max(resultado)
    exp = 1
    while maximo // exp > 0:
        resultado = _counting_sort_por_digito(resultado, exp)
        exp *= 10
    return resultado
