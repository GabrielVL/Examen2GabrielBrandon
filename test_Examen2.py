import unittest
from Examen2 import MiClase 

class TestMiClase(unittest.TestCase):

    # ------------------------------
    # Pruebas para ObtieneValencia
    # ------------------------------
    def test_ObtieneValencia_caso1(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)  # 1,3,5,7 son impares

    def test_ObtieneValencia_caso2(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.ObtieneValencia(24680)
        self.assertEqual(resultado, 0)  # ningún dígito es impar

    # ------------------------------
    # Pruebas para DivisibleTempo
    # ------------------------------
    def test_DivisibleTempo_caso1(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])

    def test_DivisibleTempo_caso2(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])  # 7 es primo