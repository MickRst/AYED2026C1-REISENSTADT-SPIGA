"""
Algoritmo de Prim para árbol de expansión mínima (MST).

Resuelve el problema de las palomas mensajeras: encontrar la forma
más eficiente de que la noticia llegue a todas las aldeas.

Complejidad: O(E log V)
"""

import heapq
from modules.grafo import Grafo, VerticeNoExisteError


class GrafoDesconectadoError(Exception):
    """El grafo no es conexo, no se pueden alcanzar todas las aldeas."""
    pass


def prim(grafo, origen):
    """
    Ejecuta Prim desde el vértice 'origen' y retorna el MST como dict de padres.

    Precondición: 'origen' es un vértice del grafo, el grafo es conexo.
    Postcondición: retorna dict donde padre[v] = (u, peso) o None si es la raíz.
                   El grafo no se modifica.

    Lanza VerticeNoExisteError si 'origen' no está en el grafo.
    Lanza GrafoDesconectadoError si el grafo no es conexo.
    """
    if not grafo.contiene_vertice(origen):
        raise VerticeNoExisteError(f"Vértice origen no encontrado: '{origen}'")

    padre = {}
    visitados = set()
    heap = [(0, origen, None)]

    while heap:
        peso, vertice, desde = heapq.heappop(heap)
        if vertice in visitados:
            continue
        visitados.add(vertice)
        padre[vertice] = (desde, peso) if desde is not None else None
        for vecino, p_arista in grafo.vecinos(vertice).items():
            if vecino not in visitados:
                heapq.heappush(heap, (p_arista, vecino, vertice))

    if len(visitados) != grafo.cantidad_vertices():
        raise GrafoDesconectadoError("El grafo no es conexo.")

    return padre


def construir_arbol_msm(padre):
    """A partir del dict de padres, arma el árbol de adyacencia del MST."""
    arbol = {v: [] for v in padre}
    for hijo, info in padre.items():
        if info is not None:
            progenitor, peso = info
            arbol[progenitor].append((hijo, peso))
    return arbol


def distancia_total_mst(padre):
    """Suma total de distancias del MST."""
    return sum(info[1] for info in padre.values() if info is not None)
