"""
Tests unitarios para el TAD Grafo y el algoritmo de Prim.
"""

import unittest
from modules.grafo import Grafo, VerticeNoExisteError, AristaInvalidaError
from modules.prim import prim, construir_arbol_msm, distancia_total_mst, GrafoDesconectadoError


def _grafo_simple():
    """
    Grafo de prueba:
        A --1-- B
        |       |
        4       2
        |       |
        C --3-- D
        A --5-- D
    MST esperado (Prim desde A): A-B(1), B-D(2), D-C(3) → total = 6
    """
    g = Grafo()
    g.agregar_arista("A", "B", 1)
    g.agregar_arista("B", "D", 2)
    g.agregar_arista("C", "D", 3)
    g.agregar_arista("A", "C", 4)
    g.agregar_arista("A", "D", 5)
    return g


class TestGrafo(unittest.TestCase):

    def test_agregar_vertice(self):
        g = Grafo()
        g.agregar_vertice("X")
        self.assertTrue(g.contiene_vertice("X"))

    def test_agregar_arista_bidireccional(self):
        g = Grafo()
        g.agregar_arista("A", "B", 10)
        self.assertIn("B", g.vecinos("A"))
        self.assertIn("A", g.vecinos("B"))
        self.assertEqual(g.vecinos("A")["B"], 10)

    def test_cantidad_vertices(self):
        g = _grafo_simple()
        self.assertEqual(g.cantidad_vertices(), 4)

    def test_cantidad_aristas(self):
        g = _grafo_simple()
        self.assertEqual(g.cantidad_aristas(), 5)

    def test_vertice_no_existe_lanza_excepcion(self):
        g = Grafo()
        with self.assertRaises(VerticeNoExisteError):
            g.vecinos("Z")

    def test_peso_invalido_lanza_excepcion(self):
        g = Grafo()
        with self.assertRaises(AristaInvalidaError):
            g.agregar_arista("A", "B", -1)
        with self.assertRaises(AristaInvalidaError):
            g.agregar_arista("A", "B", 0)

    def test_bucle_lanza_excepcion(self):
        g = Grafo()
        with self.assertRaises(AristaInvalidaError):
            g.agregar_arista("A", "A", 5)

    def test_vertice_vacio_lanza_excepcion(self):
        g = Grafo()
        with self.assertRaises(AristaInvalidaError):
            g.agregar_vertice("")

    def test_carga_desde_archivo(self):
        import tempfile, os
        contenido = "X,Y,3\nY,Z,5\n# comentario\nX,Z,8\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                         delete=False, encoding="utf-8") as f:
            f.write(contenido)
            ruta = f.name
        g = Grafo()
        g.cargar_desde_archivo(ruta)
        os.unlink(ruta)
        self.assertEqual(g.cantidad_vertices(), 3)
        self.assertEqual(g.cantidad_aristas(), 3)


class TestPrim(unittest.TestCase):

    def test_mst_correcto_distancia_total(self):
        g = _grafo_simple()
        padre = prim(g, "A")
        self.assertEqual(distancia_total_mst(padre), 6)

    def test_mst_incluye_todos_los_vertices(self):
        g = _grafo_simple()
        padre = prim(g, "A")
        self.assertEqual(set(padre.keys()), {"A", "B", "C", "D"})

    def test_origen_sin_padre(self):
        g = _grafo_simple()
        padre = prim(g, "A")
        self.assertIsNone(padre["A"])

    def test_grafo_desconectado_lanza_excepcion(self):
        g = Grafo()
        g.agregar_arista("A", "B", 1)
        g.agregar_arista("C", "D", 2)  # componente separada
        with self.assertRaises(GrafoDesconectadoError):
            prim(g, "A")

    def test_origen_inexistente_lanza_excepcion(self):
        g = _grafo_simple()
        with self.assertRaises(VerticeNoExisteError):
            prim(g, "Z")

    def test_arbol_msm_hijos(self):
        g = _grafo_simple()
        padre = prim(g, "A")
        arbol = construir_arbol_msm(padre)
        # A debe tener al menos un hijo
        self.assertTrue(len(arbol["A"]) >= 1)
        # La suma de hijos de todos los nodos = n-1 (aristas del MST)
        total_hijos = sum(len(v) for v in arbol.values())
        self.assertEqual(total_hijos, g.cantidad_vertices() - 1)

    def test_prim_aldeas_reales(self):
        """Prueba de integración con el archivo aldeas.txt."""
        import os
        ruta = os.path.join(os.path.dirname(__file__), "aldeas.txt")
        if not os.path.exists(ruta):
            self.skipTest("aldeas.txt no encontrado")
        g = Grafo()
        g.cargar_desde_archivo(ruta)
        padre = prim(g, "Peligros")
        # El MST debe incluir todos los vértices
        self.assertEqual(len(padre), g.cantidad_vertices())
        # Peligros es la raíz
        self.assertIsNone(padre["Peligros"])
        # Distancia total debe ser positiva
        self.assertGreater(distancia_total_mst(padre), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
