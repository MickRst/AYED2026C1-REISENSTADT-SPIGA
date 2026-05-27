def quicksort(lista):
    """
    Ordenamiento quicksort (recursivo).
    Precondición: lista es una lista de números.
    Postcondición: devuelve una nueva lista ordenada de menor a mayor.
    Complejidad: O(n log n) promedio.
    """
    if len(lista) <= 1:
        return lista[:]
    pivote = lista[len(lista) // 2]
    menores  = [x for x in lista if x < pivote]
    iguales  = [x for x in lista if x == pivote]
    mayores  = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)
