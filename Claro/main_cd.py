import unittest

from TestCases.test_validation_TXT_CD import TestCases_validation_TXT_CD

class Claro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_Claro_Video(self):
        print("=====> Inicio del TestCase <=====")
        tc_cd = TestCases_validation_TXT_CD()
        tc_cd.start()
        print("=====> Fin del TestCase <=====")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
    #python -m pytest main_cd.py --html=reporte_CD.html --self-contained-html