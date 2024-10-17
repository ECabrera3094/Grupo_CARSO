import unittest
import pytest
from TestCases.test_validation_TXT_CV import TestCases_validation_TXT_CV

class Claro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_Claro_Video(self):
        print("=====> Inicio del TestCase <=====")
        tc_cv = TestCases_validation_TXT_CV()
        tc_cv.start()
        print("=====> Fin del TestCase <=====")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'])
    #python -m pytest main.py --html=reporte.html --self-contained-html