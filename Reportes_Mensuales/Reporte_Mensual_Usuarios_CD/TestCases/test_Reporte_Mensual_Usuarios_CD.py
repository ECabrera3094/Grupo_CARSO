import os
from Locators.locators_Reporte_Mensual_Usuarios_CD import Locators_Reportes_Mensual_Usuarios_CD
from Queries.query_Dashboard_Reporte_Mensual import query_Dashboard
from Queries.query_Excel_License_Sold import query_Excel_License_Sold
from Queries.query_Excel_Login_Activity_Detail import query_Excel_Login_Activity_Detail

class TestCases_Reporte_Mensual_Usuarios_CD():

    def __init__(self):
        self.Download_path = Locators_Reportes_Mensual_Usuarios_CD.Download_path

        # Operations
        self.Dashboard_Suscripcion = Locators_Reportes_Mensual_Usuarios_CD.Dashboard_Suscripcion
        self.Excel_Suscripcion = Locators_Reportes_Mensual_Usuarios_CD.Excel_Suscripcion
        self.result_Suscripcion = Locators_Reportes_Mensual_Usuarios_CD.result_Suscripcion

        self.Dashboard_Licencias_Vendidas = Locators_Reportes_Mensual_Usuarios_CD.Dashboard_Licencias_Vendidas
        self.Excel_Licencias_Vendidas = Locators_Reportes_Mensual_Usuarios_CD.Excel_Licencias_Vendidas
        self.result_Licencias_Vendidas = Locators_Reportes_Mensual_Usuarios_CD.result_Licencias_Vendidas

        self.Dashboard_Login = Locators_Reportes_Mensual_Usuarios_CD.Dashboard_Login
        self.Excel_Login = Locators_Reportes_Mensual_Usuarios_CD.Excel_Login
        self.result_Login = Locators_Reportes_Mensual_Usuarios_CD.result_Login

        self.Dashboard_Licencias_Ocupadas = Locators_Reportes_Mensual_Usuarios_CD.Dashboard_Licencias_Ocupadas
        self.Excel_Licencias_Ocupadas = Locators_Reportes_Mensual_Usuarios_CD.Excel_Licencias_Ocupadas
        self.result_Licencias_Ocupadas = Locators_Reportes_Mensual_Usuarios_CD.result_Licencias_Ocupadas

        self.Dashboard_Activos = Locators_Reportes_Mensual_Usuarios_CD.Dashboard_Activos
        self.Excel_Activos = Locators_Reportes_Mensual_Usuarios_CD.Excel_Activos
        self.result_Activos = Locators_Reportes_Mensual_Usuarios_CD.result_Activos

    def test_get_data_from_dashboard(self):
        self.Dashboard_Suscripcion, self.Dashboard_Licencias_Vendidas, self.Dashboard_Licencias_Ocupadas, self.Dashboard_Login, self.Dashboard_Activos = query_Dashboard('2024 Aug')

    def test_get_license_sold(self):
        self.Excel_Suscripcion, self.Excel_Licencias_Vendidas, self.Excel_Licencias_Ocupadas = query_Excel_License_Sold('2024 Aug')

    def test_get_login_activity_detail(self):
        self.Excel_Login, self.Excel_Activos = query_Excel_Login_Activity_Detail('2024 Aug')

    def test_validations(self):
        self.result_Suscripcion = "Las Cifras para Suscripcion son Correctas" if int(self.Dashboard_Suscripcion) == int(self.Excel_Suscripcion) else f"Las Cifras para Suscripcion son Incorrectas {self.Dashboard_Suscripcion} != {self.Excel_Suscripcion}"
        print(self.result_Suscripcion)

        self.result_Licencias_Vendidas = "Las Cifras para Licencias Vendidas son Correctas" if int(self.Dashboard_Licencias_Vendidas) == int(self.Excel_Licencias_Vendidas) else f"Las Cifras para Suscripcion son Incorrectas {self.Dashboard_Licencias_Vendidas} != {self.Excel_Licencias_Vendidas}"
        print(self.result_Licencias_Vendidas)

        self.result_Licencias_Ocupadas = "Las Cifras para Licencias Ocupadas son Correctas" if int(self.Dashboard_Licencias_Ocupadas) == int(self.Excel_Licencias_Ocupadas) else f"Las Cifras para Suscripcion son Incorrectas {self.Dashboard_Licencias_Ocupadas} != {self.Excel_Licencias_Ocupadas}"
        print(self.result_Licencias_Ocupadas)

        self.result_Login = "Las Cifras para Login son Correctas" if int(self.Dashboard_Login) == int(self.Excel_Login) else f"Las Cifras para Suscripcion son Incorrectas {self.Dashboard_Login} != {self.Excel_Login}"
        print(self.result_Login)

        self.result_Activos = "Las Cifras para Activos son Correctas" if int(self.Dashboard_Activos) == int(self.Excel_Activos) else f"Las Cifras para Suscripcion son Incorrectas {self.Dashboard_Activos} != {self.Excel_Activos}"
        print(self.result_Activos)

    def test_create_report(self):

        directorio_actual = os.getcwd()
        print(f"El archivo se creará en la siguiente ruta: {directorio_actual}")
        with open(self.Download_path + "\\resultados.txt", "w") as Reporte:
            Reporte.write("Reporte Mensual de Usuarios de Claro Drive.\n")
            Reporte.write(f"Resultado Suscripcion: {self.result_Suscripcion}\n")
            Reporte.write(f"Resultado Licencias Vendidas: {self.result_Licencias_Vendidas}\n")
            Reporte.write(f"Resultado Licencias Ocupadas: {self.result_Licencias_Ocupadas}\n")
            Reporte.write(f"Resultado Login: {self.result_Login}\n")
            Reporte.write(f"Resultado Activos: {self.result_Activos}\n")