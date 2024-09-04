import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#from TestCases.test_validation_TXT_CV import TestCases_validation_TXT_CV
from TestCases.test_Reporte_Mensual_Usuarios_CD import TestCases_Reporte_Mensual_Usuarios_CD
from Locators.locators_Reporte_Mensual_Usuarios_CD import Locators_Reportes_Mensual_Usuarios_CD

class Claro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Specify Services as Driver Path
        service = Service(executable_path = Locators_Reportes_Mensual_Usuarios_CD.Drivers_path)
        # Specify Chrome Options
        options = webdriver.ChromeOptions()
        # For Chrome we ignore any Secure Certificate
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        # Specify the Path of any Download
        options.add_experimental_option('prefs', {'download.default_directory' : Locators_Reportes_Mensual_Usuarios_CD.Download_path} )
        # Start Driver
        cls.driver = webdriver.Chrome(service = service, options = options)
        cls.driver.maximize_window()
    
    def test_Claro_Video(self):
        print("=====> Inicia Creación de Reporte Mensual <=====")
        driver = self.driver
        RMUCD = TestCases_Reporte_Mensual_Usuarios_CD(driver)
        RMUCD.test_get_data_from_dashboard()
        RMUCD.test_get_license_sold()
        RMUCD.test_get_login_activity_detail()
        RMUCD.test_validate_license_sold()
        RMUCD.test_validate_login_activity()
        RMUCD.test_create_report()
        print("=====> Fin de Creación de Reporte Mensual <=====")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()