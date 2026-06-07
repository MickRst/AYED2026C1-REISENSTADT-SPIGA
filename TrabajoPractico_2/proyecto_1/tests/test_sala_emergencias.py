"""
Tests unitarios para el MinHeap genérico y la Sala de Emergencias.
"""

import unittest
from ayedfiuner.estructuras.heap import MinHeap, HeapVacioError
from modules.paciente import Paciente, NivelRiesgoInvalidoError


class TestMinHeap(unittest.TestCase):
    """Pruebas sobre el MinHeap genérico con enteros."""

    def setUp(self):
        self.heap = MinHeap()

    def test_heap_vacio_inicialmente(self):
        self.assertTrue(self.heap.esta_vacio())
        self.assertEqual(self.heap.tamanio(), 0)

    def test_insertar_un_elemento(self):
        self.heap.insertar(42)
        self.assertFalse(self.heap.esta_vacio())
        self.assertEqual(self.heap.tamanio(), 1)
        self.assertEqual(self.heap.peek(), 42)

    def test_extraer_minimo_unico(self):
        self.heap.insertar(10)
        self.assertEqual(self.heap.extraer_minimo(), 10)
        self.assertTrue(self.heap.esta_vacio())

    def test_orden_extraccion_enteros(self):
        for v in [5, 3, 8, 1, 9, 2]:
            self.heap.insertar(v)
        extraidos = [self.heap.extraer_minimo() for _ in range(6)]
        self.assertEqual(extraidos, sorted([5, 3, 8, 1, 9, 2]))

    def test_peek_no_extrae(self):
        self.heap.insertar(7)
        self.heap.insertar(3)
        self.assertEqual(self.heap.peek(), 3)
        self.assertEqual(self.heap.tamanio(), 2)

    def test_extraer_de_vacio_lanza_excepcion(self):
        with self.assertRaises(HeapVacioError):
            self.heap.extraer_minimo()

    def test_peek_de_vacio_lanza_excepcion(self):
        with self.assertRaises(HeapVacioError):
            self.heap.peek()

    def test_len(self):
        self.heap.insertar(1)
        self.heap.insertar(2)
        self.assertEqual(len(self.heap), 2)


class TestPaciente(unittest.TestCase):
    """Pruebas sobre la entidad Paciente."""

    def test_creacion_valida(self):
        p = Paciente("Ana", 1)
        self.assertEqual(p.nombre, "Ana")
        self.assertEqual(p.nivel_riesgo, 1)

    def test_nivel_invalido_lanza_excepcion(self):
        with self.assertRaises(NivelRiesgoInvalidoError):
            Paciente("X", 0)
        with self.assertRaises(NivelRiesgoInvalidoError):
            Paciente("X", 4)

    def test_comparacion_por_riesgo(self):
        critico  = Paciente("A", 1)
        moderado = Paciente("B", 2)
        self.assertTrue(critico < moderado)
        self.assertFalse(moderado < critico)

    def test_comparacion_por_turno_mismo_riesgo(self):
        p1 = Paciente("Primero",  2)
        p2 = Paciente("Segundo", 2)
        # p1 llegó antes → turno menor → tiene prioridad
        self.assertTrue(p1 < p2)


class TestSalaEmergencias(unittest.TestCase):
    """Pruebas de integración: MinHeap con Pacientes."""

    def _heap_con_pacientes(self):
        heap = MinHeap()
        heap.insertar(Paciente("Bajo1",     3))
        heap.insertar(Paciente("Crítico1",  1))
        heap.insertar(Paciente("Moderado1", 2))
        heap.insertar(Paciente("Crítico2",  1))
        heap.insertar(Paciente("Bajo2",     3))
        return heap

    def test_primero_en_atenderse_es_critico(self):
        heap = self._heap_con_pacientes()
        primero = heap.extraer_minimo()
        self.assertEqual(primero.nivel_riesgo, 1)

    def test_todos_los_criticos_antes_que_moderados(self):
        heap = self._heap_con_pacientes()
        orden = []
        while not heap.esta_vacio():
            orden.append(heap.extraer_minimo().nivel_riesgo)
        self.assertEqual(orden, sorted(orden))

    def test_fifo_dentro_mismo_nivel(self):
        heap = MinHeap()
        p1 = Paciente("PrimerModerado",  2)
        p2 = Paciente("SegundoModerado", 2)
        heap.insertar(p2)
        heap.insertar(p1)
        # p1 tiene turno menor → debe salir primero aunque se insertó después
        primero = heap.extraer_minimo()
        self.assertEqual(primero.nombre, "PrimerModerado")


if __name__ == "__main__":
    unittest.main(verbosity=2)
