import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):
    
# ------------------------------
    # Pruebas para ObtieneMasBailable
    # ------------------------------
    def test_ObtieneMasBailable_caso1(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.9)

    def test_ObtieneMasBailable_caso2(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.ObtieneMasBailable([])
        self.assertIsNone(resultado)

    # ------------------------------
    # Pruebas para VerificaListaCanciones
    # ------------------------------
    def test_VerificaListaCanciones_caso1(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.VerificaListaCanciones(["Canción 1", "Canción 2"])
        self.assertTrue(resultado)

    def test_VerificaListaCanciones_caso2(self):
        obj = MiClase(0, 0, 0, [], [])
        resultado = obj.VerificaListaCanciones(["Canción 1", None, "Canción 3"])
        self.assertFalse(resultado)


if __name__ == '_main_':
    unittest.main()