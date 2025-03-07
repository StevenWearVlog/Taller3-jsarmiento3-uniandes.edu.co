import unittest
from animal_exotico import Huron, Boa_Constrictor

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Furby", 2.5, 3, "Estados Unidos", 15.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 37.5)


class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Nagini", 20.0, 5, "Brasil", 25.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 500.0)

    def test_alimentar(self):
        self.boa.comer_raton()
        self.assertEqual(self.boa.ratones_comidos, 1)

def test_alimentar_demasiados_ratones(self):
    for _ in range(20):  # Cambiado de 10 a 20
        self.boa.comer_raton()
    with self.assertRaises(ValueError):
        self.boa.comer_raton()


if __name__ == '__main__':
    unittest.main()