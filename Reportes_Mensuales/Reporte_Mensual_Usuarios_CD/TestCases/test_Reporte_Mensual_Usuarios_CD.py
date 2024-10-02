import ssl
import smtplib 
from email.message import EmailMessage

from Queries.query_Dashboard_Reporte_Mensual import query_Dashboard
from Queries.query_Excel_License_Sold import query_Excel_License_Sold
from Queries.query_Excel_Login_Activity_Detail import query_Excel_Login_Activity_Detail

from Locators.locators_Reporte_Mensual_Usuarios_CD import Locators_Reportes_Mensual_Usuarios_CD

class TestCases_Reporte_Mensual_Usuarios_CD():

    def __init__(self):

        self.date = Locators_Reportes_Mensual_Usuarios_CD.date
        self.flag_Difference_Detected = Locators_Reportes_Mensual_Usuarios_CD.flag_Difference_Detected
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
        self.Dashboard_Suscripcion, self.Dashboard_Licencias_Vendidas, self.Dashboard_Licencias_Ocupadas, self.Dashboard_Login, self.Dashboard_Activos = query_Dashboard(self.date)

    def test_get_license_sold(self):
        self.Excel_Suscripcion, self.Excel_Licencias_Vendidas, self.Excel_Licencias_Ocupadas = query_Excel_License_Sold(self.date)

    def test_get_login_activity_detail(self):
        self.Excel_Login, self.Excel_Activos = query_Excel_Login_Activity_Detail(self.date)

    def test_validations(self):

        comparisons = [
            ("Suscripcion", self.Dashboard_Suscripcion, self.Excel_Suscripcion), 
            ("Licencias_Vendidas", self.Dashboard_Licencias_Vendidas, self.Excel_Licencias_Vendidas),
            ("Licencias_Ocupadas", self.Dashboard_Licencias_Ocupadas, self.Excel_Licencias_Ocupadas),
            ("Login", self.Dashboard_Login, self.Excel_Login),
            ("Activos", self.Dashboard_Activos, self.Excel_Activos)
        ]

        for name, value_dashboard, value_excel in comparisons:
            #print(str(value_dashboard) + "-----" + str(value_excel))
            if int(value_dashboard) == int(value_excel):
                print(f"Las Cifras para {name} son Correctas")
                setattr(self, f'result_{name}', "OK")
            else:
                print(f"Las Cifras para {name} son Incorrectas: {value_dashboard} != {value_excel}")
                setattr(self, f'result_{name}', "NO OK")
                self.flag_Difference_Detected = True

    def test_create_report(self):
        # Specify the Report Path
        with open(self.Download_path + f"\\Reporte Mensual de Usuarios de Claro Drive - {self.date}.txt", "w") as Reporte:
            # Write the Report
            Reporte.write("="*47 + "\n")
            Reporte.write("     Reporte Mensual de Usuarios - Claro Drive\n")
            Reporte.write("="*47 + "\n\n")
            Reporte.write("Resultados de las Validaciones:\n")
            Reporte.write("-" * 60 + "\n")
            Reporte.write(f"1. Suscripción              : {self.result_Suscripcion} | {self.Dashboard_Suscripcion}         | {self.Excel_Suscripcion}\n")
            Reporte.write(f"2. Licencias Vendidas       : {self.result_Licencias_Vendidas} | {self.Dashboard_Licencias_Vendidas}         | {self.Excel_Licencias_Vendidas}\n")
            Reporte.write(f"3. Licencias Ocupadas       : {self.result_Licencias_Ocupadas} | {self.Dashboard_Licencias_Ocupadas}          | {self.Excel_Licencias_Ocupadas}\n")
            Reporte.write(f"4. Login                    : {self.result_Login} | {self.Dashboard_Login}          | {self.Excel_Login}\n")
            Reporte.write(f"5. Usuarios Activos         : {self.result_Activos} | {self.Dashboard_Activos}           | {self.Excel_Activos}\n")
            Reporte.write("-" * 60 + "\n\n")
            Reporte.write("Fin del Reporte.\n")
            Reporte.write("="*50 + "\n")
            Reporte.close()

    def test_send_email(self):
        # Specify the Email Configuration
        msg = EmailMessage()
        # Specify the Subject - Title
        # If Flags is True, We suffer an Invalid Numerical Figure
        if self.flag_Difference_Detected:
            msg["Subject"] = "Reporte Mensual de Usuarios de Claro Drive - NO OK"
        else:
            msg["Subject"] = "Reporte Mensual de Usuarios de Claro Drive - OK"
        # Specify the Email Body
        msg.set_content("Reciban un Saludo:\nEn el Archivo Adjunto recibirán las validaciones correspondientes al Reporte Mensual de Usuarios de CD.\n¡Saludos!\nDashboard: https://amco.cloud.looker.com/dashboards/1628")
        msg["From"] = "pruebasl735@hotmail.com"
        # List of multiple Recipients
        recipients = ["cabrerapereze@hotmail.com"] # "sanchezgd@globalhitss.com", "bellaje@globalhitss.com", , "sanchezgd@globalhitss.com"
        msg["To"] = ", ".join(recipients)

        with open(self.Download_path + f"\\Reporte Mensual de Usuarios de Claro Drive - {self.date}.txt", 'rb') as content_file:
            # Read the Content of the File
            content = content_file.read()
            # Attach the File to the Email
            msg.add_attachment(content, maintype='application', subtype='txt', filename='Resultados.txt')
        # This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption 
        # and peer authentication facilities for network sockets, both client-side and server-side
        context=ssl.create_default_context()

        # Specify the Server
        with smtplib.SMTP("smtp.office365.com", port=587) as smtp:
            # Email Communication can be Encrypted with TLS
            smtp.starttls(context = context)
            # Enter User, Password
            smtp.login(msg["From"], "Calidad007.")
            # Send Email
            smtp.send_message(msg)