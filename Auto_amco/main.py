import unittest
from tests.test_semanalCVMAX import testSemanal

class AutoAmcoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_semanalCVMAX(self):
        print("=====> Inicia la revisión <=====")
        tc_cvmax = testSemanal()
        print("=====> Fin de la prueba <=====")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()