"""
tests/test_ordenamiento.py
Pruebas unitarias para los algoritmos de ordenamiento:
burbuja, quicksort y radix_sort.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import unittest
import random
from biblioteca_ayed_fiuner.ayedfiuner.algoritmos.ordenamiento import (
    burbuja, quicksort, radix_sort
)


class TestBurbuja(unittest.TestCase):

    def test_lista_500_elementos(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        self.assertEqual(burbuja(lista), sorted(lista))


class TestQuicksort(unittest.TestCase):

    def test_lista_500_elementos(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        self.assertEqual(quicksort(lista), sorted(lista))


class TestRadixSort(unittest.TestCase):

    def test_lista_500_elementos(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        self.assertEqual(radix_sort(lista), sorted(lista))


if __name__ == '__main__':
    unittest.main()