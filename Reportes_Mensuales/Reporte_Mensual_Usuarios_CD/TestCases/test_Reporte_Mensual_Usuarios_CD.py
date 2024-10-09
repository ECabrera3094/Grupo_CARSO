import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        from_email = 'usuarioshitsss@gmail.com'
        password = 'sgxc uknf fibw xbfy'
        report_file = self.Download_path + f"\\Reporte Mensual de Usuarios de Claro Drive - {self.date}.txt"

        # Specify the Subject - Title
        # If Flags is True, We suffer an Invalid Numerical Figure
        if self.flag_Difference_Detected:
            subject = "Reporte Mensual de Usuarios de Claro Drive - NO OK"
        else:
            subject = "Reporte Mensual de Usuarios de Claro Drive - OK"
        # Specify the Email Body
        body = "Reciban un Saludo:\nEn el Archivo Adjunto recibirán las validaciones correspondientes al Reporte Mensual de Usuarios de CD.\n¡Saludos!\nAtte: Emiliano <3\nDashboard: https://amco.cloud.looker.com/dashboards/1628"

        """
        MIMEMultipart es una clase en el módulo email.mime.multipart de Python que se utiliza para crear mensajes de correo electrónico 
        que contienen contenido mixto. Esto es especialmente útil cuando deseas enviar un correo que tenga tanto texto como
        archivos adjuntos, o diferentes tipos de contenido como texto plano y adjuntos HTML.
        """
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = 'cabreraemi@globalhitss.com'
        msg['Subject'] = subject

        # Especifica que el tipo de contenido es texto plano sin ningún tipo de formato como HTML.
        msg.attach(MIMEText(body, 'plain'))

        # Attach the File to the Email
        # rb - Read Binary lecture Mode
        with open(report_file, 'rb') as attachment:
            """
            MIMEBASE : Clase base que se usa para manejar archivos genéricos/binarios en email, como documentos, archivos comprimidos, o cualquier tipo de archivo adjunto.
            'application': Indica que el archivo adjunto es de tipo "application", para archivos que no son solo texto (TXT, PDF, imágenes).
            'octet-stream': Indica que es un flujo de datos binarios (no texto), para cualquier tipo de archivo que no sea texto simple.
            """
            part = MIMEBase('application', 'octet-stream')
            # Lee el contenido binario del archivo abierto y lo establece como el "payload" (carga útil) de la parte MIME.
            part.set_payload(attachment.read())
            # Base64 convierte datos binarios en texto seguro para la transmisión.
            encoders.encode_base64(part)
            # Add a Header
            part.add_header('Content-Disposition', # Informs the mail client that this is an attachment.
                            f'attachment; filename = {os.path.basename(report_file)}' # The attachment is just a file withoute the complete path.
                            )
            msg.attach(part)

        # Specify the Server
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                # Enter User, Password
                server.login(from_email, password)
                server.send_message(msg)
                print("Envío de Email Exitoso!")
        except Exception as e:
            print(f"Error al Enviar el Email: {e}")