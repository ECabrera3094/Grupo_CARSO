from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
from configuration.configuration import Configuration
from configuration.locatorsLooker import locator
import logging
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


class testSemanal:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('Inicia test Reporte semanal CVMAX')
        self.config = Configuration()
        self.locators = locator()
        self.inicioTest()
        self.navegaPagina()
        self.descargaArchivo()
        self.consultaBQ()
        self.validaResultado()
        self.resultados()
        self.send_email()

    def resultados(self):
           # Write the Report

           file_name = "C:/Auto_amco/reportes/Resultados_CVMAX/semanalCVMAX.txt"
           with open(file_name, 'w') as file:
            #print("=" * 47 + "\n\n")
            #Resultados
                file.write('======== **REPORTE SEMANAL CVMAX** ========\n')
                file.write(f"Resultados:\n")
                file.write("-" * 60 + "\n")
                file.write(f"{'Categoría':<20} {'Looker':<15} {'BQ':<15}\n")
                file.write("-" * 60 + "\n")
                file.write(f"{'Activos:':<20} {self.total_Activos:<15} {self.total_activos:<15}\n")
                file.write(f"{'Cancelados:':<20} {self.total_Cancelados:<15} {self.total_Cancelaciones:<15}\n")
                file.write(f"{'Transacciones:':<20} {self.total_Transacciones:<15} {self.total_transacciones:<15}\n")
                file.write(f"{'Usuarios Únicos:':<20} {self.totaltransaccionesUnicas:<15} {self.totaltransaccionesUnicas:<15}\n")
                file.write("-" * 60 + "\n\n")
                file.write("Fin del Reporte.\n")
                file.write("=" * 50 + "\n")

    def inicioTest(self):
        self.config.inicia_pagina()
        if self.config.driver is None:
            raise Exception("Driver no inicializado. Asegúrate de que inicia_pagina() fue llamado correctamente.")

        self.logger.info('Se instancia la configuración del driver')
        try:
            WebDriverWait(self.config.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.locators.boton_acceder))
            )
        #    print('1.- Ingreso a producción')
        except TimeoutException as toe:
            print("Timeout Error en la carga de la página: ", toe)

        self.config.driver.find_element(By.ID, self.locators.textbox_user).send_keys(self.locators.Loocker_user)
        self.config.driver.find_element(By.ID, self.locators.id_textbox_password).send_keys(self.locators.Loocker_password)
        self.config.driver.find_element(By.ID, self.locators.boton_acceder).click()

    def navegaPagina(self):
        #print('2.- Ingreso al reporte Telcel CVMAX')
        try:
            WebDriverWait(self.config.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.locators.xpath_reportes_homologados))
            )
        except TimeoutException as toe:
            print("Timeout Error en la carga de la página: ", toe)

        self.config.driver.find_element(By.XPATH, self.locators.xpath_reportes_homologados).click()
        sleep(2)
        self.config.driver.find_element(By.XPATH, self.locators.xpath_claro_video).click()
        sleep(2)
        self.config.driver.find_element(By.XPATH, self.locators.xpath_finanzas).click()
        sleep(2)
        self.config.driver.find_element(By.XPATH, self.locators.xpath_archivos_CVMAX).click()
        sleep(2)
        self.config.driver.find_element(By.XPATH, self.locators.xpath_archivos_operaciones_CVMAX).click()
        sleep(2)

        try:
            WebDriverWait(self.config.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.locators.xpath_confirmación_de_reporte))
            )
            assert self.config.driver.find_element(By.XPATH, self.locators.xpath_confirmación_de_reporte).is_displayed(), 'El reporte no es visible.'
            #self.config.driver.save_screenshot('Dentro del reporte telcelCVMAX.png')
        except TimeoutException as toe:
            assert False, "Timeout: No se pudo encontrar el elemento esperado."
            #self.config.driver.save_screenshot('Falla de carga del reporte telcelCVMAX.png')

        try:
            WebDriverWait(self.config.driver, timeout=10).until(
                EC.visibility_of_element_located((By.XPATH, self.locators.xpath_reportesDisponibles))
            )
            assert self.config.driver.find_element(By.XPATH, self.locators.xpath_reportesDisponibles).is_displayed(), 'Archivos no visibles'
        except TimeoutException as toe:
            assert False, "Timeout: No se pudo encontrar el elemento esperado."
            self.config.driver.save_screenshot('No cargo la lista de archivos.png')

    def descargaArchivo(self):
        # Configuración del navegador
        self.config.chrome_options = Options()
        self.config.chrome_options.add_experimental_option('prefs', {
            'download.default_directory': str(self.locators.Download_path),
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        })

        #print('3.- Descarga del archivo')
        WebDriverWait(self.config.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.xpath_descarga_archivo))
        )
        self.config.driver.find_element(By.XPATH, self.locators.xpath_descarga_archivo).click()
        sleep(5)
        print(f"Descargando en: {self.locators.Download_path}")

        # Espera hasta que la descarga se complete
        while True:
            # Busca archivos temporales de Chrome
            chrome_temp_file = sorted(Path(self.locators.Download_path).glob('*.crdownload'))
            temp_file = sorted(Path(self.locators.Download_path).glob('*.tmp'))
            
            # Si hay archivos temporales, sigue esperando
            if chrome_temp_file or temp_file:
                #print('Archivo descargado.')
                sleep(5)
            else:
                break

        #print('Se termina la descarga ...\n\n')

        print("-------- **REPORTE SEMANAL CVMAX** --------")
                # Cerrar el navegador
        self.config.driver.close()
        self.config.driver.quit()

        file_cvmax = sorted(Path(self.locators.Download_path).glob('*.xlsx'))
        #Contenido del archivo (todas las solapas)
        today = datetime.today()
        formatted_date = today.strftime('%Y/%m/%d')  # Formato AAAA/MM/DD
        print(f'\nFECHA DEL REPORTE:\n{formatted_date}')

        if file_cvmax:
            total_from_excel = {}

            # Leer la hoja "Activos"
            activos_df = pd.read_excel(file_cvmax[0], sheet_name='Activos')
            self.total_Activos = activos_df.shape[0]
            assert self.total_Activos > 0, 'El total de registros en "Activos" debe ser mayor que 0.'
            print(f'Looker_Total Activos: {self.total_Activos}')

            # Leer la hoja "Cancelados"
            try:
                cancelados_df = pd.read_excel(file_cvmax[0], sheet_name='Cancelados')
                self.total_Cancelados = cancelados_df.shape[0]
                assert self.total_Cancelados > 0, 'El total de registros en "Cancelados" debe ser mayor que 0.'
                total_from_excel['Cancelados'] = self.total_Cancelados  # Guarda el total en el diccionario
                print(f'Looker_Total Cancelados: {self.total_Cancelados}')
            except ValueError as e:
                print(f'Error al leer la hoja "Cancelados": {e}')

            # Leer la hoja "Transacciones"
            try:
                transacciones_df = pd.read_excel(file_cvmax[0], sheet_name='Transacciones')
                self.total_Transacciones = transacciones_df.shape[0]
                assert self.total_Transacciones > 0, 'El total de registros en "Transacciones" debe ser mayor que 0.'
                total_from_excel['Transacciones'] = self.total_Transacciones  # Guarda el total en el diccionario
                print(f'Looker_Total Transacciones: {self.total_Transacciones}')
            except ValueError as e:
                print(f'Error al leer la hoja "Transacciones": {e}')
        else:
            print("No se encontró ningún archivo Excel.")

        # Lectura de usuarios únicos transacciones
        if file_cvmax:
            uut = 'Usuarios Unicos Transacciones'
            try:
                dat = pd.read_excel(file_cvmax[0], sheet_name=uut)
                self.total_usuario_unicos = dat.shape[1]
                assert self.total_usuario_unicos > 0, 'El total de registros en "Usuarios Unicos Transacciones" debe ser mayor que 0.'
                total_from_excel[uut] = self.total_usuario_unicos

                # print(f'Looker_Total Usuarios Únicos: {self.total_usuario_unicos}')

                if self.total_usuario_unicos > 1:
                    # print("Lista de Usuarios Únicos:")
                    pass
                else:
                    # print("Looker Total Usuarios Únicos:")
                    pass

                for index, row in dat.iterrows():
                    print(f"Looker Total Usuarios Únicos{row['USUARIOS_UNICOS_TRANSACCIONES']}")
                    pass

            except ValueError as e:
                print(f'Error al leer la hoja: "{uut}": {e}')

    def consultaBQ(self):
        from google.cloud import bigquery
        client = bigquery.Client()

        # Resultados de Activos
        query = """SELECT COUNT(1) AS total FROM amco-cv-qa.GRAL.FAC_CVMAX_ACTIVOS"""
        query_job = client.query(query)
        results = query_job.result()

        for row in results:
            self.total_activos = row[0]
            print(f"BQ_Total Activos: {self.total_activos}")


        # Resultados de Cancelaciones
        query = """SELECT COUNT(1) AS total FROM amco-cv-qa.GRAL.FAC_CVMAX_CANCELACIONES"""
        query_job = client.query(query)
        results = query_job.result()

        for row in results:
            self.total_Cancelaciones = row[0]  # Acceder al primer elemento de la fila
            print(f"BQ_Total Cancelaciones: {self.total_Cancelaciones}")
            

        # Resultados de Transacciones
        query = """SELECT COUNT(1) AS total FROM amco-cv-qa.GRAL.FAC_CVMAX_TRANSACCIONES"""
        query_job = client.query(query)
        results = query_job.result()

        for row in results:
            self.total_transacciones = row[0]
            print(f"BQ_Total Transacciones: {self.total_transacciones}")

        # Resultados de Usuarios Únicos Transacciones
        query = """SELECT COUNT(DISTINCT(CAST(USUARIO_ID AS INT64))) AS USUARIOS_UNICOS_TRANSACCIONES FROM amco-cv-qa.GRAL.FAC_CVMAX_TRANSACCIONES"""
        query_job = client.query(query)
        results = query_job.result()

        for row in results:
            self.totaltransaccionesUnicas = row[0]
            print(f"BQ_Total Usuarios Únicos: {self.totaltransaccionesUnicas}")

    def validaResultado(self):
        try:
            assert self.total_Activos == self.total_activos, (
                f'Discrepancia en Total Activos: Looker: {self.total_Activos}, BQ: {self.total_activos}'
            )
            assert self.total_Cancelados == self.total_Cancelaciones, (
                f'Discrepancia en Total Cancelados: Looker: {self.total_Cancelados}, BQ: {self.total_Cancelaciones}'
            )
            assert self.total_Transacciones == self.total_transacciones, (
                f'Discrepancia en Total Transacciones: Looker: {self.total_Transacciones}, BQ: {self.total_transacciones}'
            )
            #assert self.total_usuario_unicos == self.totaltransaccionesUnicas, (
            #    f'Discrepancia en Total Transacciones: Looker: {self.total_usuario_unicos}, BQ: {self.totaltransaccionesUnicas}'
            #)

            # Si todas las aserciones pasan, la prueba es exitosa
            print(" ")
            return True  # Retorna True si todas las validaciones son exitosas
        except AssertionError as e:
            # Manejo de errores si alguna aserción falla
            print(f"Error en la validación: {e}")
            return False  # Retorna False si alguna aserción falla

    def send_email(self):
        from_email = 'usuarioshitsss@gmail.com'
        password = 'sgxc uknf fibw xbfy'
        report_file = "C:/Auto_amco/reportes/Resultados_CVMAX/semanalCVMAX.txt"

        # Validacion del resultado
        if self.validaResultado():
            subject = 'Prueba Exitosa - Estatus prueba semanal CVMAX'
            body = 'Las validaciones fueron exitosas.'
        else:
            subject = 'Prueba No Exitosa - Estatus prueba semanal CVMAX'
            body = 'Las validaciones no fueron exitosas.'

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = 'team_gcp@clarovideotv.com'
        #msg['To'] = 'cabreraemi@globalhitss.com'
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with open(report_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(report_file)}',
            )
            msg.attach(part)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(from_email, password)
                server.send_message(msg)
                # print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")