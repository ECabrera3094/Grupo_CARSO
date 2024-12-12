import pytest

from TestCases.test_Plan_Brasil import TestCases_Plan_Brasil

class TestClaro():

    @classmethod
    def setUpClass(cls):
        pass

    def test_Claro_Video(self):
        print("\n=====> Inicio del TestCase <=====")
        pb = TestCases_Plan_Brasil()
        pb.validate_Plan_Brasil()
        print("=====> Fin del TestCase <=====")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    pytest.main()

# pytest test_reproceso.py --param1=HOLA --param2=Hola --capture=no