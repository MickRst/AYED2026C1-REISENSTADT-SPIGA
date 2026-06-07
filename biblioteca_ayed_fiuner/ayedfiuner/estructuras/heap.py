"""
TAD MinHeap - Montículo binario de mínimos.

El elemento más pequeño siempre queda en la raíz.
Se representa internamente como una lista donde para el nodo en índice i:
    - hijo izquierdo: 2*i + 1
    - hijo derecho:   2*i + 2
    - padre:          (i - 1) // 2

Complejidades:
    insertar:      O(log n)
    extraer_min:   O(log n)
    peek:          O(1)
"""


class HeapVacioError(Exception):
    pass


class MinHeap:

    def __init__(self):
        self._datos = []

    def insertar(self, elemento):
        """
        Precondición: el elemento es comparable con los del heap.
        Postcondición: el elemento queda en el heap, propiedad de heap se mantiene.
        """
        self._datos.append(elemento)
        self._subir(len(self._datos) - 1)

    def extraer_minimo(self):
        """
        Precondición: el heap no está vacío.
        Postcondición: se remueve y retorna el mínimo, propiedad de heap se mantiene.
        Lanza HeapVacioError si está vacío.
        """
        if self.esta_vacio():
            raise HeapVacioError("No se puede extraer de un heap vacío.")
        self._datos[0], self._datos[-1] = self._datos[-1], self._datos[0]
        minimo = self._datos.pop()
        if not self.esta_vacio():
            self._bajar(0)
        return minimo

    def peek(self):
        """
        Precondición: el heap no está vacío.
        Postcondición: retorna el mínimo sin modificar el heap.
        Lanza HeapVacioError si está vacío.
        """
        if self.esta_vacio():
            raise HeapVacioError("El heap está vacío.")
        return self._datos[0]

    def esta_vacio(self):
        return len(self._datos) == 0

    def tamanio(self):
        return len(self._datos)

    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self._datos[i] < self._datos[padre]:
                self._datos[i], self._datos[padre] = self._datos[padre], self._datos[i]
                i = padre
            else:
                break

    def _bajar(self, i):
        n = len(self._datos)
        while True:
            menor = i
            izq = 2 * i + 1
            der = 2 * i + 2
            if izq < n and self._datos[izq] < self._datos[menor]:
                menor = izq
            if der < n and self._datos[der] < self._datos[menor]:
                menor = der
            if menor != i:
                self._datos[i], self._datos[menor] = self._datos[menor], self._datos[i]
                i = menor
            else:
                break

    def __len__(self):
        return self.tamanio()

    def __repr__(self):
        return f"MinHeap({self._datos})"
