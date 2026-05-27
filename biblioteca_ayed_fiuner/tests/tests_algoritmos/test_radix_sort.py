import unittest
import random
from ayedfiuner.algoritmos.radix_sort import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_lista_500_elementos(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        self.assertEqual(radix_sort(lista), sorted(lista))

if __name__ == '__main__':
    unittest.main()
