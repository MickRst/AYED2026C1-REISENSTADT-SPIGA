"""
TAD Grafo no dirigido con pesos.
Representado como lista de adyacencia (diccionario de diccionarios).
"""


class VerticeNoExisteError(KeyError):
    pass


class AristaInvalidaError(ValueError):
    pass


class Grafo:
    """
    Grafo no dirigido y ponderado.
    Internamente: self._adyacencia[u][v] = peso (y también [v][u] = peso)
    """

    def __init__(self):
        self._adyacencia = {}

    def agregar_vertice(self, vertice):
        """
        Precondición: vertice es un string no vacío.
        Postcondición: el vértice existe en el grafo.
        """
        if not vertice:
            raise AristaInvalidaError("El nombre del vértice no puede ser vacío.")
        if vertice not in self._adyacencia:
            self._adyacencia[vertice] = {}

    def agregar_arista(self, origen, destino, peso):
        """
        Agrega arista no dirigida entre origen y destino con el peso dado.
        Si los vértices no existen se crean solos.

        Precondición: peso > 0, origen != destino.
        Postcondición: la arista queda en ambas direcciones.
        Lanza AristaInvalidaError si peso <= 0 o hay bucle.
        """
        if peso <= 0:
            raise AristaInvalidaError(f"El peso debe ser positivo. Recibido: {peso}")
        if origen == destino:
            raise AristaInvalidaError("No se permiten bucles.")
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self._adyacencia[origen][destino] = peso
        self._adyacencia[destino][origen] = peso

    def vecinos(self, vertice):
        """
        Retorna {vecino: peso} del vértice.
        Lanza VerticeNoExisteError si no existe.
        """
        if vertice not in self._adyacencia:
            raise VerticeNoExisteError(f"Vértice no encontrado: '{vertice}'")
        return self._adyacencia[vertice]

    def vertices(self):
        return list(self._adyacencia.keys())

    def aristas(self):
        """Retorna lista de (u, v, peso) sin duplicados."""
        vistas = set()
        resultado = []
        for u, vecinos in self._adyacencia.items():
            for v, peso in vecinos.items():
                par = tuple(sorted([u, v]))
                if par not in vistas:
                    vistas.add(par)
                    resultado.append((u, v, peso))
        return resultado

    def cantidad_vertices(self):
        return len(self._adyacencia)

    def cantidad_aristas(self):
        return len(self.aristas())

    def contiene_vertice(self, vertice):
        return vertice in self._adyacencia

    def cargar_desde_archivo(self, ruta):
        """
        Carga aristas desde archivo. Formato por línea: origen,destino,peso
        Las líneas con '#' se ignoran.

        Precondición: el archivo existe y es legible.
        Postcondición: todas las aristas válidas quedan en el grafo.
        """
        with open(ruta, "r", encoding="utf-8") as f:
            for num, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                partes = linea.split(",")
                if len(partes) != 3:
                    continue  # ignorar líneas incompletas (ej: nombre de aldea sin aristas)
                origen, destino, peso_str = (p.strip() for p in partes)
                try:
                    self.agregar_arista(origen, destino, int(peso_str))
                except ValueError:
                    raise AristaInvalidaError(f"Línea {num}: distancia no entera: {peso_str!r}")

    def __repr__(self):
        return f"Grafo(vértices={self.cantidad_vertices()}, aristas={self.cantidad_aristas()})"
