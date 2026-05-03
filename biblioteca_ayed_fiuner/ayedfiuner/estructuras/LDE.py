class IndexOutOfRangeError(Exception):
    """Excepción personalizada para índices fuera de rango."""
    pass


class _Nodo:
    """
    Nodo interno de la lista doblemente enlazada.
    Cada nodo guarda un dato y referencias al nodo anterior y siguiente.
    """
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDobleEnlazada:
    """
    TAD Lista Doblemente Enlazada.
    Permite almacenar elementos comparables (int, float, str, etc).
    """

    def __init__(self):
        """
        Inicializa la lista vacía.
        Postcondición: la lista no tiene elementos, cabeza y cola son None.
        """
        self._cabeza = None
        self._cola = None
        self._tamanio = 0

    # ── Properties ──────────────────────────────────────────────────────────

    @property
    def cabeza(self):
        """Devuelve el nodo cabeza (primer nodo) de la lista."""
        return self._cabeza

    @property
    def cola(self):
        """Devuelve el nodo cola (último nodo) de la lista."""
        return self._cola

    @property
    def tamanio(self):
        """Devuelve el tamaño de la lista (acceso público)."""
        return self._tamanio

    # ── Métodos principales ──────────────────────────────────────────────────

    def esta_vacia(self):
        """
        Devuelve True si la lista no tiene elementos.
        Postcondición: no modifica la lista.
        """
        return self._tamanio == 0

    def agregar_al_inicio(self, item):
        """
        Agrega un nuevo ítem al inicio de la lista.
        Postcondición: el ítem queda como primer elemento. Complejidad O(1).
        """
        nuevo = _Nodo(item)
        if self.esta_vacia():
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo
            self._cabeza = nuevo
        self._tamanio += 1

    def agregar_al_final(self, item):
        """
        Agrega un nuevo ítem al final de la lista.
        Postcondición: el ítem queda como último elemento. Complejidad O(1).
        """
        nuevo = _Nodo(item)
        if self.esta_vacia():
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.anterior = self._cola
            self._cola.siguiente = nuevo
            self._cola = nuevo
        self._tamanio += 1

    def insertar(self, item, posicion=None):
        """
        Agrega un ítem en la posición indicada (0-indexado).
        Si no se indica posición, agrega al final.
        Precondición: posición debe ser un entero entre 0 y len(lista).
        Postcondición: el ítem queda en la posición indicada.
        Lanza IndexOutOfRangeError si la posición es inválida.
        """
        if posicion is None:
            self.agregar_al_final(item)
            return

        if not isinstance(posicion, int) or posicion < 0 or posicion > self._tamanio:
            raise IndexOutOfRangeError(
                f"Posición {posicion} inválida para lista de tamaño {self._tamanio}."
            )

        if posicion == 0:
            self.agregar_al_inicio(item)
            return

        if posicion == self._tamanio:
            self.agregar_al_final(item)
            return

        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        nuevo = _Nodo(item)
        anterior = actual.anterior
        anterior.siguiente = nuevo
        nuevo.anterior = anterior
        nuevo.siguiente = actual
        actual.anterior = nuevo
        self._tamanio += 1

    def extraer(self, posicion=None):
        """
        Elimina y devuelve el ítem en la posición indicada.
        Si no se indica posición, elimina y devuelve el último elemento.
        Precondición: la lista no debe estar vacía.
                      posición debe ser un entero entre 0 y len(lista)-1.
        Postcondición: el ítem en 'posición' es eliminado de la lista.
        Lanza IndexOutOfRangeError si la posición es inválida.
        Complejidad O(1) para extraer del inicio o del final.
        """
        if self.esta_vacia():
            raise IndexOutOfRangeError("No se puede extraer de una lista vacía.")

        if posicion is None:
            posicion = self._tamanio - 1

        # Soporte para índice -1 (último elemento), como en Python estándar
        if posicion == -1:
            posicion = self._tamanio - 1

        if not isinstance(posicion, int) or posicion < 0 or posicion >= self._tamanio:
            raise IndexOutOfRangeError(
                f"Posición {posicion} inválida para lista de tamaño {self._tamanio}."
            )

        # Extraer el primero → O(1)
        if posicion == 0:
            dato = self._cabeza.dato
            self._cabeza = self._cabeza.siguiente
            if self._cabeza is not None:
                self._cabeza.anterior = None
            else:
                self._cola = None
            self._tamanio -= 1
            return dato

        # Extraer el último → O(1)
        if posicion == self._tamanio - 1:
            dato = self._cola.dato
            self._cola = self._cola.anterior
            if self._cola is not None:
                self._cola.siguiente = None
            else:
                self._cabeza = None
            self._tamanio -= 1
            return dato

        # Caso general
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        self._tamanio -= 1
        return actual.dato

    def copiar(self):
        """
        Devuelve una copia nueva de la lista, elemento a elemento.
        Postcondición: la lista original no se modifica.
        Complejidad O(n): se recorre la lista una sola vez.
        """
        nueva = ListaDobleEnlazada()
        actual = self._cabeza
        while actual is not None:
            nueva.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva

    def invertir(self):
        """
        Invierte el orden de los elementos de la lista en su lugar.
        Postcondición: el primer elemento pasa a ser el último y viceversa.
        Complejidad O(n).
        """
        actual = self._cabeza
        self._cabeza, self._cola = self._cola, self._cabeza
        while actual is not None:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior

    def concatenar(self, otra_lista):
        """
        Agrega al final de esta lista todos los elementos de otra_lista.
        Precondición: otra_lista debe ser una ListaDobleEnlazada.
        Postcondición: esta lista contiene sus elementos originales
                       más los de otra_lista al final.
        """
        actual = otra_lista.cabeza
        while actual is not None:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    # ── Métodos especiales (dunder) ──────────────────────────────────────────

    def __len__(self):
        """
        Devuelve la cantidad de elementos de la lista. Complejidad O(1).
        """
        return self._tamanio

    def __add__(self, otra_lista):
        """
        Suma dos listas: devuelve una nueva lista con los elementos de ambas.
        Usa copiar() y concatenar() internamente.
        """
        nueva = self.copiar()
        nueva.concatenar(otra_lista)
        return nueva

    def __iter__(self):
        """
        Permite recorrer la lista con un ciclo for.
        Devuelve el dato de cada nodo, no el nodo en sí.
        """
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __repr__(self):
        """Representación de la lista para imprimir fácilmente."""
        elementos = []
        actual = self._cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "ListaDoble([" + " ↔ ".join(elementos) + "])"
