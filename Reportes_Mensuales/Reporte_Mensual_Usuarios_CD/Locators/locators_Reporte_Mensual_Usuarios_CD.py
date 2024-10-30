import calendar
from datetime import datetime

class Locators_Reportes_Mensual_Usuarios_CD():

    def generate_date():
        month = calendar.month_name[datetime.now().month - 1][0:3]
        year = datetime.now().year if datetime.now().month != 1 else datetime.now().year - 1
        new_date = f"{year} {month}"
        return new_date

    #Download_path = "/tmp/" # Sólo aplica al Proyecto en la Nube
    Download_path = "C:\\Automation\\Reportes_Mensuales\\Reporte_Mensual_Usuarios_CD\\Downloads"


    Dashboard_Suscripcion = 0
    Excel_Suscripcion = 0
    result_Suscripcion = 0

    Dashboard_Licencias_Vendidas = 0
    Excel_Licencias_Vendidas = 0
    result_Licencias_Vendidas = 0

    Dashboard_Login = 0
    Excel_Login = 0
    result_Login = 0

    Dashboard_Licencias_Ocupadas = 0
    Excel_Licencias_Ocupadas = 0
    result_Licencias_Ocupadas = 0

    Dashboard_Activos = 0
    Excel_Activos = 0
    result_Activos = 0

    date = generate_date()

    flag_Difference_Detected = 0