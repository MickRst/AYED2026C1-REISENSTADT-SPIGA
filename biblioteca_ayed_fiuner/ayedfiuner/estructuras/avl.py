"""
Árbol AVL - árbol binario de búsqueda auto-balanceado.

Claves y valores pueden ser de cualquier tipo comparable.
Todas las operaciones principales son O(log n).
"""

from __future__ import annotations
from typing import Any, Optional


class ClaveNoEncontradaError(KeyError):
    pass


class ArbolVacioError(Exception):
    pass


class _Nodo:
    __slots__ = ("clave", "valor", "izq", "der", "altura")

    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolAVL:
    """
    Árbol AVL genérico.
    Para todo nodo, la diferencia de alturas entre subárbol izquierdo
    y derecho es como máximo 1.
    """

    def __init__(self):
        self._raiz = None
        self._tamanio = 0

    def insertar(self, clave, valor):
        """
        Inserta o actualiza el par (clave, valor).

        Precondición: la clave es comparable con las demás del árbol.
        Postcondición: el árbol contiene (clave, valor) y la propiedad AVL se mantiene.
        """
        insertado = [False]
        self._raiz = self._insertar(self._raiz, clave, valor, insertado)
        if insertado[0]:
            self._tamanio += 1

    def buscar(self, clave):
        """
        Precondición: la clave existe en el árbol.
        Postcondición: retorna el valor sin modificar el árbol.
        Lanza ClaveNoEncontradaError si no existe.
        """
        nodo = self._buscar_nodo(self._raiz, clave)
        if nodo is None:
            raise ClaveNoEncontradaError(f"Clave no encontrada: {clave!r}")
        return nodo.valor

    def eliminar(self, clave):
        """
        Precondición: la clave existe en el árbol.
        Postcondición: el nodo es removido y la propiedad AVL se mantiene.
        Lanza ClaveNoEncontradaError si no existe.
        """
        if self._buscar_nodo(self._raiz, clave) is None:
            raise ClaveNoEncontradaError(f"Clave no encontrada: {clave!r}")
        self._raiz = self._eliminar(self._raiz, clave)
        self._tamanio -= 1

    def contiene(self, clave):
        return self._buscar_nodo(self._raiz, clave) is not None

    def en_rango(self, clave_min, clave_max):
        """Genera (clave, valor) en orden para claves en [clave_min, clave_max]."""
        yield from self._en_rango(self._raiz, clave_min, clave_max)

    def maximo_en_rango(self, clave_min, clave_max):
        valores = [v for _, v in self.en_rango(clave_min, clave_max)]
        if not valores:
            raise ArbolVacioError("No hay datos en el rango especificado.")
        return max(valores)

    def minimo_en_rango(self, clave_min, clave_max):
        valores = [v for _, v in self.en_rango(clave_min, clave_max)]
        if not valores:
            raise ArbolVacioError("No hay datos en el rango especificado.")
        return min(valores)

    def tamanio(self):
        return self._tamanio

    def esta_vacio(self):
        return self._raiz is None

    # ── Métodos internos ──────────────────────────────────────────────

    @staticmethod
    def _altura(nodo):
        return nodo.altura if nodo else 0

    @staticmethod
    def _balance(nodo):
        if nodo is None:
            return 0
        return ArbolAVL._altura(nodo.izq) - ArbolAVL._altura(nodo.der)

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

    def _rotar_derecha(self, y):
        x = y.izq
        t2 = x.der
        x.der = y
        y.izq = t2
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    def _rotar_izquierda(self, x):
        y = x.der
        t2 = y.izq
        y.izq = x
        x.der = t2
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    def _balancear(self, nodo, clave):
        self._actualizar_altura(nodo)
        bal = self._balance(nodo)
        if bal > 1 and clave < nodo.izq.clave:
            return self._rotar_derecha(nodo)
        if bal < -1 and clave > nodo.der.clave:
            return self._rotar_izquierda(nodo)
        if bal > 1 and clave > nodo.izq.clave:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if bal < -1 and clave < nodo.der.clave:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)
        return nodo

    def _insertar(self, nodo, clave, valor, insertado):
        if nodo is None:
            insertado[0] = True
            return _Nodo(clave, valor)
        if clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave, valor, insertado)
        elif clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, clave, valor, insertado)
        else:
            nodo.valor = valor
            return nodo
        return self._balancear(nodo, clave)

    def _buscar_nodo(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo
        if clave < nodo.clave:
            return self._buscar_nodo(nodo.izq, clave)
        return self._buscar_nodo(nodo.der, clave)

    def _minimo_nodo(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return None
        if clave < nodo.clave:
            nodo.izq = self._eliminar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self._eliminar(nodo.der, clave)
        else:
            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq
            sucesor = self._minimo_nodo(nodo.der)
            nodo.clave = sucesor.clave
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar(nodo.der, sucesor.clave)

        self._actualizar_altura(nodo)
        bal = self._balance(nodo)
        if bal > 1 and self._balance(nodo.izq) >= 0:
            return self._rotar_derecha(nodo)
        if bal > 1 and self._balance(nodo.izq) < 0:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if bal < -1 and self._balance(nodo.der) <= 0:
            return self._rotar_izquierda(nodo)
        if bal < -1 and self._balance(nodo.der) > 0:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)
        return nodo

    def _en_rango(self, nodo, clave_min, clave_max):
        if nodo is None:
            return
        if clave_min < nodo.clave:
            yield from self._en_rango(nodo.izq, clave_min, clave_max)
        if clave_min <= nodo.clave <= clave_max:
            yield (nodo.clave, nodo.valor)
        if clave_max > nodo.clave:
            yield from self._en_rango(nodo.der, clave_min, clave_max)
