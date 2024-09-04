import requests
import polars as pl
import pandas as pd
import os
import time
import zipfile
import pyarrow
import datetime
import itertools
import pandas as pd
from pyarrow import csv
import pyarrow.parquet
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

from Locators.locators_Reporte_Mensual_Usuarios_CD import Locators_Reportes_Mensual_Usuarios_CD

class TestCases_Reporte_Mensual_Usuarios_CD():

    def __init__(self, driver):
        self.driver = driver

        self.Drivers_path = Locators_Reportes_Mensual_Usuarios_CD.Drivers_path

        self.Loocker_URL = Locators_Reportes_Mensual_Usuarios_CD.Loocker_URL
        self.Loocker_user = Locators_Reportes_Mensual_Usuarios_CD.Loocker_user
        self.Loocker_password = Locators_Reportes_Mensual_Usuarios_CD.Loocker_password

        self.Looker_Reporte_Mensual_Usuarios_URL = Locators_Reportes_Mensual_Usuarios_CD.Looker_Reporte_Mensual_Usuarios_URL
        self.Looker_Licencias_Vendidas_URL = Locators_Reportes_Mensual_Usuarios_CD.Looker_Licencias_Vendidas_URL
        self.Looker_Login_Actividad_Detalle_URL = Locators_Reportes_Mensual_Usuarios_CD.Looker_Login_Actividad_Detalle_URL

        self.id_textbox_user = Locators_Reportes_Mensual_Usuarios_CD.id_textbox_user
        self.id_textbox_password = Locators_Reportes_Mensual_Usuarios_CD.id_textbox_password
        self.id_loging_button = Locators_Reportes_Mensual_Usuarios_CD.id_loging_button
        self.xpath_shared_link = Locators_Reportes_Mensual_Usuarios_CD.xpath_shared_link
        self.xpath_dashboard_table = Locators_Reportes_Mensual_Usuarios_CD.xpath_dashboard_table
        self.xpath_date_close_icon = Locators_Reportes_Mensual_Usuarios_CD.xpath_date_close_icon
        self.xpath_date_textbox = Locators_Reportes_Mensual_Usuarios_CD.xpath_date_textbox
        self.xpath_actualizar_button = Locators_Reportes_Mensual_Usuarios_CD.xpath_actualizar_button
        self.xpath_three_dots_menu = Locators_Reportes_Mensual_Usuarios_CD.xpath_three_dots_menu
        self.xpath_delete_cache_and_refresh = Locators_Reportes_Mensual_Usuarios_CD.xpath_delete_cache_and_refresh
        self.xpath_Suscripcion = Locators_Reportes_Mensual_Usuarios_CD.xpath_Suscripcion
        self.xpath_Licencias_Vendidas = Locators_Reportes_Mensual_Usuarios_CD.xpath_Licencias_Vendidas
        self.xpath_Login = Locators_Reportes_Mensual_Usuarios_CD.xpath_Login
        self.xpath_Licenias_Ocupadas = Locators_Reportes_Mensual_Usuarios_CD.xpath_Licenias_Ocupadas
        self.xpath_Activos = Locators_Reportes_Mensual_Usuarios_CD.xpath_Activos

        self.xpath_dashboard_table_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_dashboard_table_2
        self.xpath_date_close_icon_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_date_close_icon_2
        self.xpath_date_textbox_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_date_textbox_2
        self.xpath_actualizar_button_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_actualizar_button_2
        self.xpath_three_dots_menu_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_three_dots_menu_2
        self.xpath_delete_cache_and_refresh_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_delete_cache_and_refresh_2
        self.xpath_descargar_datos_button_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_descargar_datos_button_2
        self.xpath_formato_menu_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_formato_menu_2
        self.xpath_opciones_avanzadas_menu_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_opciones_avanzadas_menu_2
        self.xpath_todos_los_resultados_menu_2 = Locators_Reportes_Mensual_Usuarios_CD.xpath_todos_los_resultados_menu_2
        self.id_descarga_button_2 = Locators_Reportes_Mensual_Usuarios_CD.id_descarga_button_2

        self.xpath_dashboard_table_3 = Locators_Reportes_Mensual_Usuarios_CD.xpath_dashboard_table_3
        self.xpath_three_dots_menu_3 = Locators_Reportes_Mensual_Usuarios_CD.xpath_three_dots_menu_3
        self.xpath_delete_cache_and_refresh_3 = Locators_Reportes_Mensual_Usuarios_CD.xpath_delete_cache_and_refresh_3
        self.xpath_descargar_datos_button_3 = Locators_Reportes_Mensual_Usuarios_CD.xpath_descargar_datos_button_3
        self.xpath_formato_menu_3 = Locators_Reportes_Mensual_Usuarios_CD.xpath_formato_menu_3
        self.xpath_opciones_avanzadas_menu_3 = Locators_Reportes_Mensual_Usuarios_CD.xpath_opciones_avanzadas_menu_3
        self.xpath_todos_los_resultados_menu_3 = Locators_Reportes_Mensual_Usuarios_CD.xpath_todos_los_resultados_menu_3
        self.id_descarga_button_3 = Locators_Reportes_Mensual_Usuarios_CD.id_descarga_button_3

        self.Download_path = Locators_Reportes_Mensual_Usuarios_CD.Download_path

        # Operations
        self.int_Suscripcion = Locators_Reportes_Mensual_Usuarios_CD.int_Suscripcion
        self.int_Licencias_Vendidas = Locators_Reportes_Mensual_Usuarios_CD.int_Licencias_Vendidas
        self.int_Login = Locators_Reportes_Mensual_Usuarios_CD.int_Login
        self.int_Licencias_Ocupadas = Locators_Reportes_Mensual_Usuarios_CD.int_Licencias_Ocupadas
        self.int_Activos = Locators_Reportes_Mensual_Usuarios_CD.int_Activos
        self.errors = Locators_Reportes_Mensual_Usuarios_CD.errors

    def test_get_data_from_dashboard(self):
        # Get to Looker URL
        self.driver.get(self.Loocker_URL)

        # Validate the Login Page based on the User Textbox
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, self.id_textbox_user))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)

        # Enter Username
        self.driver.find_element(By.ID, self.id_textbox_user).send_keys(self.Loocker_user)

        # Enter Password
        self.driver.find_element(By.ID, self.id_textbox_password).send_keys(self.Loocker_password)

        # Click Login Button
        self.driver.find_element(By.ID, self.id_loging_button).click()

        # Validate the Succesess Login
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, self.xpath_shared_link))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)

        # Get to the Dashboard 1031 - Reporte Mensual
        self.driver.get(self.Looker_Reporte_Mensual_Usuarios_URL)

        # Validate the Existence of the Dashboard Table
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, self.xpath_dashboard_table))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)

        # Press Close on Year-Month If is necesary.
        try:
            self.driver.find_element(By.XPATH, self.xpath_date_close_icon).click()
        except:
            pass

        # Click on the Date Textbox
        self.driver.find_element(By.XPATH, self.xpath_date_textbox).click()
        time.sleep(2)

        # Enter the Date
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform() 

        # Click on "Actualizar"
        self.driver.find_element(By.XPATH, self.xpath_actualizar_button).click()
        time.sleep(10)

        # Save Screenshot

        # -----
        actions.scroll_to_element("/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[4]/div/section/div/div[1]/div/button/div[2]")
        # --- Refresh Cache and Update Page
        # Click on 3 Dots
        self.driver.find_element(By.XPATH, self.xpath_three_dots_menu).click()
        time.sleep(1)

        # Click on Delete Caché and Refresh
        self.driver.find_element(By.XPATH, self.xpath_delete_cache_and_refresh).click()
        time.sleep(10)

        # -----
        # Obtain the Values of the Table
        self.int_Suscripcion = self.driver.find_element(By.XPATH, self.xpath_Suscripcion).text
        self.int_Suscripcion = int(self.int_Suscripcion.replace(',', ''))

        self.int_Licencias_Vendidas = self.driver.find_element(By.XPATH, self.xpath_Licencias_Vendidas).text
        self.int_Licencias_Vendidas = int(self.int_Licencias_Vendidas.replace(',', ''))

        self.int_Login = self.driver.find_element(By.XPATH, self.xpath_Login).text
        self.int_Login = int(self.int_Login.replace(',', ''))

        self.int_Licencias_Ocupadas = self.driver.find_element(By.XPATH, self.xpath_Licenias_Ocupadas).text
        self.int_Licencias_Ocupadas = int(self.int_Licencias_Ocupadas.replace(',', ''))

        self.int_Activos = self.driver.find_element(By.XPATH, self.xpath_Activos).text
        self.int_Activos = int(self.int_Activos.replace(',', ''))

        print("Suscripcion: ", self.int_Suscripcion)

        print("Licencias Vendidas:", self.int_Licencias_Vendidas)

        print("Login: ", self.int_Login)

        print("Licencias Ocuapadas: ", self.int_Licencias_Ocupadas)

        print("Activos: ", self.int_Activos)

    def test_get_license_sold(self):
        # Geto to Licenses Sold Dashboard
        self.driver.get(self.Looker_Licencias_Vendidas_URL)

        # Validate the Existence of the Dashboard Table
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.xpath_dashboard_table_2))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)

        # Press close on Year-Month If is necesary.
        try:
            self.driver.find_element(By.XPATH, self.xpath_date_close_icon_2).click()
        except:
            pass

        # Click on the Date Textbox
        self.driver.find_element(By.XPATH, self.xpath_date_textbox_2).click()
        time.sleep(3)

        # Enter the Date
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER).perform() 
        
        # Click on "Actualizar"
        self.driver.find_element(By.XPATH, self.xpath_actualizar_button_2).click()
        time.sleep(3)

        # Wait the Table
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[3]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]"))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)

        # Click on 3 dots
        self.driver.find_element(By.XPATH, self.xpath_three_dots_menu_2).click()
        time.sleep(3)

        # Click on Delete Cache & Refresh
        #self.driver.find_element(By.XPATH, self.xpath_delete_cache_and_refresh_2).click()
        #time.sleep(10)

        # Click on 3 dots
        #self.driver.find_element(By.XPATH, self.xpath_three_dots_menu_2).click()
        #time.sleep(3)

        # Click on Download Data
        self.driver.find_element(By.XPATH, self.xpath_descargar_datos_button_2).click()
        time.sleep(3)

        # Click on Format
        self.driver.find_element(By.XPATH, self.xpath_formato_menu_2).click()
        time.sleep(3)

        # Down to Excel
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform() 
        time.sleep(3)

        # Click on Advance Options
        self.driver.find_element(By.XPATH, self.xpath_opciones_avanzadas_menu_2).click()
        time.sleep(3)

        # Click on All the Results
        self.driver.find_element(By.XPATH, self.xpath_todos_los_resultados_menu_2).click()
        time.sleep(3)

        # Click on Download Button
        self.driver.find_element(By.ID, self.id_descarga_button_2).click()
        time.sleep(40)

    def test_get_login_activity_detail(self):
        # Get to Login Activity Detail Dashboard
        self.driver.get(self.Looker_Login_Actividad_Detalle_URL)

        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, self.xpath_dashboard_table_3))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)

        ###
        # FALTA SELECCIONAR LA FECHA
        date_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div[1]/div/span/span"
        self.driver.find_element(By.XPATH, date_button).click()
        time.sleep(1)
        close_button = "/html/body/div[3]/div/div/div/div/div/div/div/div/div[1]/span/button/div[2]"
        try:
            self.driver.find_element(By.XPATH, close_button).click()
            time.sleep(1)
        except:
            pass
        
        date_value = "/html/body/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div"
        self.driver.find_element(By.XPATH, date_value).click()

        # Enter the Date
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER).perform() 

        time.sleep(5)

        ####

        refresh_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/div/button"
        self.driver.find_element(By.XPATH, refresh_button).click()
        time.sleep (10)

        # Click on 3 dots
        self.driver.find_element(By.XPATH, self.xpath_three_dots_menu_3).click()
        time.sleep(3)

        # Descargar Datos
        self.driver.find_element(By.XPATH, self.xpath_descargar_datos_button_3).click()
        time.sleep(3)

        # Click on Formato
        self.driver.find_element(By.XPATH, self.xpath_formato_menu_3).click()
        time.sleep(3)

        # Down to Excel
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform() 
        time.sleep(3)

        # Click on Opciones Avanzadas
        self.driver.find_element(By.XPATH, self.xpath_opciones_avanzadas_menu_3).click() 
        time.sleep(3)

        # Click on Todos los Resultados
        self.driver.find_element(By.XPATH, self.xpath_todos_los_resultados_menu_3).click()
        time.sleep(3)

        # Click on Download
        self.driver.find_element(By.ID, self.id_descarga_button_3).click()
        time.sleep(40)

    def test_validate_license_sold(self):
        
        os.listdir(self.Download_path)

        df = pd.read_excel("C:\\Automation\\Reportes_Mensuales\\Reporte_Mensual_Usuarios_CD\\Downloads\\Licencias vendidas asignadas detalle.xlsx", engine='openpyxl')
        
        # ----- Sumar los valores de la columna 'Suscripciones'
        sum_Suscripciones = int(df["Suscripciones"].sum())

        print(f"Suma de la columna 'Suscripciones': {sum_Suscripciones}")
        
        try:
            assert int(sum_Suscripciones) == int(self.int_Suscripcion) # Excel vs Dashbaod
        except AssertionError as ae:
            print(f"Error: {ae}")
            self.errors.append(str(ae))

        # ----- Sumar los valores de la columna 'Licencias'
        sum_Licencias_Vendidas = int(df["Licencias"].sum())

        print(f"Suma de la columna 'Licencias Vendidas': {sum_Licencias_Vendidas}")

        try:
            assert int(sum_Licencias_Vendidas) == int(self.int_Licencias_Vendidas) # Excel vs Dashbaod
        except AssertionError as ae:
            print(f"Error: {ae}")
            self.errors.append(str(ae))

        # ----- Sumar los valores de la columna 'Buzones'
        sum_Buzones = int(df["Buzones"].sum())

        print(f"Suma de la columna 'Buzones': {sum_Buzones}")

        try:
            assert int(sum_Buzones) == int(self.int_Licencias_Ocupadas) # Excel vs Dashbaod
        except AssertionError as ae:
            print(f"Error: {ae}")
            self.errors.append(str(ae))

        print(self.errors)

    def test_validate_login_activity(self):

        os.listdir(self.Download_path)

        df = pd.read_excel("C:\\Automation\\Reportes_Mensuales\\Reporte_Mensual_Usuarios_CD\\Downloads\\Login actividad.xlsx", engine='openpyxl')

        # ----- Sumar los valores de la columna 'Activo'
        sum_Activo = (df['Activo'] == 'SI').sum()

        print(f"Suma de la columna 'Activas': {sum_Activo}")

        try:
            assert int(sum_Activo) == int(self.int_Activos) # Excel vs Dashbaod
        except AssertionError as ae:
            print(f"Error: {ae}")
            self.errors.append(str(ae))

        # ----- Sumar los valores de la columna 'Activo'
        sum_Login = int(df["Login"].sum())

        print(f"Suma de la columna 'Login': {sum_Login}")

        try:
            assert int(sum_Login) == int(self.int_Login) # Excel - 5 vs Dashbaod
        except AssertionError as ae:
            print(f"Error: {ae}")
            self.errors.append(str(ae))

        print(self.errors)

    def test_create_report(self):

        # Define el nombre del archivo PDF
        report_path = self.Download_path + "\\Reporte.pdf"

        # Crea el documento PDF
        document = SimpleDocTemplate(report_path, pagesize=letter)

        # Define los estilos para el texto
        styles = getSampleStyleSheet()
        normal_style = styles['Normal']
        heading_style = styles['Heading1']

        # Puedes personalizar los estilos
        custom_style = ParagraphStyle(
            'CustomStyle',
            parent=normal_style,
            fontName='Helvetica-Bold',
            fontSize=14,
            leading=24,
            spaceAfter=12
        )

        # Define el contenido del PDF
        content = []

        # Agrega un encabezado
        header = Paragraph("Reporte Mensual de Usuarios de Claro Drive", heading_style)
        content.append(header)

        # Agrega un párrafo con formato personalizado
        paragraph = Paragraph("Este es un párrafo de ejemplo con <b>negrita</b> y <i>cursiva</i>.", custom_style)
        content.append(paragraph)

        content.append(Paragraph(str(self.int_Suscripcion)))
        content.append(Paragraph(str(self.int_Licencias_Vendidas)))
        content.append(Paragraph(str(self.int_Login)))
        content.append(Paragraph(str(self.int_Licencias_Ocupadas)))
        content.append(Paragraph(str(self.int_Activos)))
        content.append(Paragraph(str(self.errors)))

        # Construye el PDF
        document.build(content)

        print(f"Archivo PDF '{report_path}' creado exitosamente.")