import unittest

from TestCases.test_Reporte_Mensual_Usuarios_CD import TestCases_Reporte_Mensual_Usuarios_CD

class Claro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_Reporte(self):
        print("\n=====> Inicia Creación de Reporte Mensual <=====")
        RMUCD = TestCases_Reporte_Mensual_Usuarios_CD()
        RMUCD.test_get_data_from_dashboard()
        RMUCD.test_get_license_sold()
        RMUCD.test_get_login_activity_detail()
        RMUCD.test_validations()
        RMUCD.test_create_report()
        RMUCD.test_send_email()
        print("\n=====> Finaliza Creación de Reporte Mensual <=====")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()