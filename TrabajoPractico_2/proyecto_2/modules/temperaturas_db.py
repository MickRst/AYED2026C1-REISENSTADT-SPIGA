"""
Módulo Temperaturas_DB

Base de datos en memoria para almacenar mediciones de temperatura
indexadas por fecha, usando un árbol AVL internamente.

Formato de fecha: "dd/mm/aaaa"
"""

from datetime import datetime, date
from ayedfiuner.estructuras.avl import ArbolAVL, ClaveNoEncontradaError, ArbolVacioError


class FechaInvalidaError(ValueError):
    """Formato de fecha incorrecto."""
    pass


class FechaNoEncontradaError(KeyError):
    """No existe medición para la fecha dada."""
    pass


class RangoInvalidoError(ValueError):
    """fecha1 debe ser menor que fecha2."""
    pass


_FORMATO = "%d/%m/%Y"


def _parsear_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, _FORMATO).date()
    except (ValueError, TypeError):
        raise FechaInvalidaError(
            f"Formato de fecha inválido: '{fecha_str}'. Use 'dd/mm/aaaa'."
        )


def _validar_rango(f1, f2):
    if f1 >= f2:
        raise RangoInvalidoError("fecha1 debe ser estrictamente menor que fecha2.")


class TemperaturaDB:
    """
    Base de datos de temperaturas indexada por fecha.
    Usa un ArbolAVL donde la clave es datetime.date y el valor es float (°C).

    Complejidades:
        guardar_temperatura, devolver_temperatura, borrar_temperatura: O(log n)
        max/min/extremos/devolver en rango: O(log n + k), k = nodos en el rango
        cantidad_muestras: O(1)
    """

    def __init__(self):
        self._arbol = ArbolAVL()

    def guardar_temperatura(self, temperatura, fecha):
        """
        Guarda o actualiza la temperatura para una fecha.

        Precondición: fecha con formato 'dd/mm/aaaa', temperatura es un número.
        Postcondición: la medición queda en el árbol.
        Lanza FechaInvalidaError si el formato es incorrecto.
        """
        clave = _parsear_fecha(fecha)
        self._arbol.insertar(clave, float(temperatura))

    def devolver_temperatura(self, fecha):
        """
        Retorna la temperatura registrada en la fecha dada.

        Precondición: existe una medición para la fecha.
        Postcondición: el árbol no se modifica.
        Lanza FechaNoEncontradaError si no existe la fecha.
        """
        clave = _parsear_fecha(fecha)
        try:
            return self._arbol.buscar(clave)
        except ClaveNoEncontradaError:
            raise FechaNoEncontradaError(f"No hay medición para: {fecha}")

    def borrar_temperatura(self, fecha):
        """
        Elimina la medición de la fecha dada.

        Precondición: existe una medición para la fecha.
        Postcondición: la medición es removida del árbol.
        Lanza FechaNoEncontradaError si no existe la fecha.
        """
        clave = _parsear_fecha(fecha)
        try:
            self._arbol.eliminar(clave)
        except ClaveNoEncontradaError:
            raise FechaNoEncontradaError(f"No hay medición para: {fecha}")

    def max_temp_rango(self, fecha1, fecha2):
        """
        Precondición: fecha1 < fecha2, formato 'dd/mm/aaaa'.
        Postcondición: retorna la temperatura máxima del rango, árbol sin cambios.
        Lanza RangoInvalidoError o ArbolVacioError si no hay datos.
        """
        f1, f2 = _parsear_fecha(fecha1), _parsear_fecha(fecha2)
        _validar_rango(f1, f2)
        return self._arbol.maximo_en_rango(f1, f2)

    def min_temp_rango(self, fecha1, fecha2):
        """
        Precondición: fecha1 < fecha2, formato 'dd/mm/aaaa'.
        Postcondición: retorna la temperatura mínima del rango, árbol sin cambios.
        Lanza RangoInvalidoError o ArbolVacioError si no hay datos.
        """
        f1, f2 = _parsear_fecha(fecha1), _parsear_fecha(fecha2)
        _validar_rango(f1, f2)
        return self._arbol.minimo_en_rango(f1, f2)

    def temp_extremos_rango(self, fecha1, fecha2):
        """
        Retorna (min, max) en el rango dado en un solo recorrido.

        Precondición: fecha1 < fecha2.
        Postcondición: retorna tupla (min, max), árbol sin cambios.
        """
        f1, f2 = _parsear_fecha(fecha1), _parsear_fecha(fecha2)
        _validar_rango(f1, f2)
        valores = [v for _, v in self._arbol.en_rango(f1, f2)]
        if not valores:
            raise ArbolVacioError("No hay datos en el rango especificado.")
        return min(valores), max(valores)

    def devolver_temperaturas(self, fecha1, fecha2):
        """
        Retorna lista de strings 'dd/mm/aaaa: temperatura ºC' ordenadas por fecha.

        Precondición: fecha1 < fecha2.
        Postcondición: árbol sin cambios.
        """
        f1, f2 = _parsear_fecha(fecha1), _parsear_fecha(fecha2)
        _validar_rango(f1, f2)
        resultado = []
        for clave, valor in self._arbol.en_rango(f1, f2):
            resultado.append(f"{clave.strftime(_FORMATO)}: {valor} ºC")
        return resultado

    def cantidad_muestras(self):
        """Retorna la cantidad de muestras almacenadas. O(1)."""
        return self._arbol.tamanio()

    def cargar_desde_archivo(self, ruta):
        """
        Lee un archivo con formato 'dd/mm/aaaa,temperatura' por línea.
        Las líneas con '#' se ignoran.

        Precondición: el archivo existe y es legible.
        Postcondición: las mediciones válidas quedan en el árbol.
        Retorna la cantidad de registros cargados.
        """
        cargados = 0
        errores = 0
        with open(ruta, "r", encoding="utf-8") as f:
            for num, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                partes = linea.split(",")
                if len(partes) != 2:
                    errores += 1
                    continue
                try:
                    self.guardar_temperatura(float(partes[1].strip()), partes[0].strip())
                    cargados += 1
                except (FechaInvalidaError, ValueError):
                    errores += 1
        print(f"  Carga finalizada: {cargados} registros OK, {errores} errores.")
        return cargados
