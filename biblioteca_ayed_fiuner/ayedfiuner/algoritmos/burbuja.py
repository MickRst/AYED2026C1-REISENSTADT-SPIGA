def burbuja(lista):
    """
    Ordenamiento burbuja.
    Precondición: lista es una lista de números.
    Postcondición: devuelve una nueva lista ordenada de menor a mayor.
    Complejidad: O(n²).
    """
    resultado = lista[:]
    n = len(resultado)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    return resultado
