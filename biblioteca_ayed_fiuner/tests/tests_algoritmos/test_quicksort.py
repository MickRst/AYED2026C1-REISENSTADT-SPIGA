import unittest
import random
from ayedfiuner.algoritmos.quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_lista_500_elementos(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        self.assertEqual(quicksort(lista), sorted(lista))

if __name__ == '__main__':
    unittest.main()
