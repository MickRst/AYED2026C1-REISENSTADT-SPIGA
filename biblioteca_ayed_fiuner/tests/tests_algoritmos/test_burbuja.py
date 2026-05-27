import unittest
import random
from ayedfiuner.algoritmos.burbuja import burbuja

class TestBurbuja(unittest.TestCase):
    def test_lista_500_elementos(self):
        lista = [random.randint(10000, 99999) for _ in range(500)]
        self.assertEqual(burbuja(lista), sorted(lista))

if __name__ == '__main__':
    unittest.main()
