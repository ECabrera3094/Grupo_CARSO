import unittest
import sys
from TestCases.test_validation_TXT_CV import TestCases_validation_TXT_CV

class Claro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_Claro_Video(self):
        # valor1 = int(sys.argv[1])
        # if valor1 == 20240925:
        #     print("OK")
        # valor2 = int(sys.argv[2])
        # valor3 = sys.argv[3] # "MX, BR"
        # print(type(valor3)) # tipo string
        # print(f"El valor 1 es {valor1}")
        # print(f"El valor 2 es {valor2}")
        # print(f"El valor 3 es {valor3}")
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