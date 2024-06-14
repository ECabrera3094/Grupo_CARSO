import unittest

from TestCases.test_validation_TXT_CV import TestCases_validation_TXT_CV

class Claro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_Claro_Video(self):
        print("=====> Inicio del TestCase <=====")
        tc = TestCases_validation_TXT_CV()
        tc.start()
        print("=====> Fin del TestCase <=====")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
    #python -m pytest main.py --html=reporte.html