import unittest

from TestCases.test_validation_TXT_LOGIN import TestCases_validation_TXT_LOGIN

class Claro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_Claro_Video(self):
        print("\n=====> Inicio del TestCase <=====")
        tc_login = TestCases_validation_TXT_LOGIN()
        tc_login.start()
        print("=====> Fin del TestCase <=====")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
    #python -m pytest main_login.py --html=reporte_LOGIN.html --self-contained-html