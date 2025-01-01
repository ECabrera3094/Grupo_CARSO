import calendar

from datetime import datetime

class Locators_Reportes_Mensual_Usuarios_CD():

    def generate_date():
        # Obtenemos la Fecha
        now = datetime.now()
        # Calcula el Mes Anterior:
        # - now.month - 1: Resta 1 al mes actual.
        # - % 12: Asegura que el resultado esté dentro del rango 1-12 (Enero -> Diciembre).
        # - or 12: Si el resultado es 0 (por ejemplo, 1 - 1 = 0), cambia a 12 (Diciembre).
        prev_month = (now.month - 1) % 12 or 12
        # Ajusta el Año si el Mes actual es Enero:
        # Si estamos en Enero (now.month == 1), resta 1 al Año Actual.
        # Para otros Meses, el Año no Cambia.
        prev_year = now.year - (1 if now.month == 1 else 0)
        # Obtiene el nombre abreviado del mes anterior:
        # calendar.month_name[prev_month] Obtiene el nombre completo del mes anterior.
        # [:3] Toma los primeros tres caracteres para obtener la abreviatura.
        new_date = f"{prev_year} {calendar.month_name[prev_month][:3]}"
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