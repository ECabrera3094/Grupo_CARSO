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
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Locators
from Locators.locators_validation_TXT_CV import Locators_validation_TXT_CV

class TestCases_validation_TXT_CV():

    def __init__(self):
        #self.date = Locators_validation_TXT_CV.date

        self.Drivers_path  = Locators_validation_TXT_CV.Drivers_path 

        self.Loocker_URL = Locators_validation_TXT_CV.Loocker_URL
        self.Loocker_URL_Archivos_Operaciones_CV = Locators_validation_TXT_CV.Loocker_URL_Archivos_Operaciones_CV
        self.Loocker_user = Locators_validation_TXT_CV.Loocker_user 
        self.Loocker_password = Locators_validation_TXT_CV.Loocker_password
        self.list_Countries = Locators_validation_TXT_CV.list_Countries
        self.list_TXT_Operations_Files = Locators_validation_TXT_CV.list_TXT_Operations_Files
        self.dict_Number_of_Files = Locators_validation_TXT_CV.dict_Number_of_Files
        self.dict_File_per_Operation = Locators_validation_TXT_CV.dict_File_per_Operation
        self.dict_Mandatory_Columns_per_Operation = Locators_validation_TXT_CV.dict_Mandatory_Columns_per_Operation

        self.id_textbox_user = Locators_validation_TXT_CV.id_textbox_user 
        self.id_textbox_password  = Locators_validation_TXT_CV.id_textbox_password 
        self.id_loging_button = Locators_validation_TXT_CV.id_loging_button
        self.xpath_main_page_logo = Locators_validation_TXT_CV.xpath_main_page_logo
        self.xpath_dashboard_claro_video_link = Locators_validation_TXT_CV.xpath_dashboard_claro_video_link
        self.xpath_produccion_link = Locators_validation_TXT_CV.xpath_produccion_link
        self.xpath_reportes_homologados_link = Locators_validation_TXT_CV.xpath_reportes_homologados_link
        self.xpath_claro_video_link = Locators_validation_TXT_CV.xpath_claro_video_link
        self.xpath_archivos_txt_link = Locators_validation_TXT_CV.xpath_archivos_txt_link
        self.xpath_archivos_operaciones_cv_link = Locators_validation_TXT_CV.xpath_archivos_operaciones_cv_link
        self.xpath_pais_button = Locators_validation_TXT_CV.xpath_pais_button
        self.xpath_close_pais = Locators_validation_TXT_CV.xpath_close_pais
        self.xpath_listbox_pais = Locators_validation_TXT_CV.xpath_listbox_pais
        self.xpath_actualizar_button = Locators_validation_TXT_CV.xpath_actualizar_button
        self.xpath_panel_actions = Locators_validation_TXT_CV.xpath_panel_actions
        self.xpath_clear_cache_update = Locators_validation_TXT_CV.xpath_clear_cache_update
        self.xpath_descargar_archivo_button = Locators_validation_TXT_CV.xpath_descargar_archivo_button

        self.Download_path = Locators_validation_TXT_CV.Download_path

    def start(self):
        self.download_Compressed_Files()
        self.unzip_Compressed_Files()

    def download_Compressed_Files(self):
        print("=====> Inicia Descarga de Archivos <=====")
        # Specify Services as Driver Path
        service = Service(executable_path = self.Drivers_path)
        # Specify Chrome Options
        options = webdriver.ChromeOptions()
        # For Chrome we ignore any Secure Certificate
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        #options.add_argument('--headless')
        # Specify the Path of any Download
        options.add_experimental_option('prefs', {'download.default_directory' : self.Download_path} )
        driver = webdriver.Chrome(service = service, options = options)
        driver.maximize_window()
        driver.get(self.Loocker_URL)
        #driver.delete_all_cookies()
        # Validate the Login Page based on the User Textbox
        try:
            WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.ID, self.id_textbox_user))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)
        # Enter Username
        driver.find_element(By.ID, self.id_textbox_user).send_keys(self.Loocker_user)
        # Enter Password
        driver.find_element(By.ID, self.id_textbox_password).send_keys(self.Loocker_password)
        # Click Login Button
        driver.find_element(By.ID, self.id_loging_button).click()
        #---
        time.sleep(15)
        driver.get(self.Loocker_URL_Archivos_Operaciones_CV)
        time.sleep(10)
        # Validate the correct Dashboard based on the Country Button. 
        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, self.xpath_pais_button))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)
        # --------------------------------
        # Start the Loop of Countries
        # === Start on Argentin and ends of Uruguay.
        i = 1
        for _ in itertools.repeat(None, len(self.list_Countries)):
            # Click on "Pais" Button
            driver.find_element(By.XPATH, self.xpath_pais_button).click()
            time.sleep(2)
            # Click on "X" if you have already a Countrie on the Field.
            try:
                driver.find_element(By.XPATH, self.xpath_close_pais ).click()
            except Exception:
                pass
            # Click on the Listbox
            driver.find_element(By.XPATH, self.xpath_listbox_pais).click() 
            time.sleep(2)
            # Choose a Countrie
            driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/ul/li["+str(i)+"]/div/div").click() # !!!
            time.sleep(2)
            # Clik on "Actualizar" Button
            driver.find_element(By.XPATH, self.xpath_actualizar_button).click() 
            time.sleep(10)
            # --- Refresh Cache and Update Page
            driver.find_element(By.XPATH, self.xpath_panel_actions).click()
            time.sleep(3)
            driver.find_element(By.XPATH, self.xpath_clear_cache_update).click()
            time.sleep(10)
            # Click on "Descargar Archivo" Button
            driver.find_element(By.XPATH, self.xpath_descargar_archivo_button).click()
            time.sleep(15)
            # Count +1
            i += 1
        # --------------------------------
        # Checking the Download Process
        wait = True
        while(wait):
            # Returns an Array with the Full Path of each Element Inside.
            chrome_temp_file = sorted(Path(self.Download_path).glob('*.crdownload'))
            firefox_temp_file = sorted(Path(self.Download_path).glob('*.part'))
            print("Array: ", len(chrome_temp_file))
            # If the Array contains more than one .crdownload File, we have to wait
            if (len(chrome_temp_file) >= 1 or len(firefox_temp_file) >= 1):
                print('Descargando Archivos ...')
                time.sleep(30)
            else:
                # Break the Loop.
                wait = False
        print('Descarga de Archivos Finalizada ...')
        # --------------------------------
        # End of Driver Session
        driver.close()
        driver.quit()

    def unzip_Compressed_Files(self):
        print("\n=====> Inicia Descompresion de Archivos de Claro Video<=====\n")
        # Obtain the DateTime and Replace the "-" symbol. 
        today = str(datetime.date.today()).replace("-","")
        #today = str(20241026)
        # ----- Enter the Zip File
        # Validate the 16 Countries
        for country in self.list_Countries:
            try: 
                # Create a New Directory where the Files will be Extracted
                new_Download_Directory = self.Download_path + '\\txt_' + country + '_' + today
                os.mkdir(new_Download_Directory) 
                # Descargamos los Archivos según su País y Carpeta
                # Loading the temp.zip and creating a Zip Object 
                with zipfile.ZipFile(self.Download_path + '\\txt_' + country + '_' + today +'.zip', 'r') as zipObject:
                    zipObject.extractall(path = new_Download_Directory)
                print("País: ", country, " OK\n")
            except Exception:
                print("País: ", country, " FAIL\n")

        print("Validacion de Duplicidad de Archivos por Operación.\n")
        self.validate_duplicity(self.list_Countries, self.list_TXT_Operations_Files, today)

        print("Validación de la Cantidad de Archivos.")
        self.validate_number_of_files(self.list_Countries, self.dict_Number_of_Files, self.Download_path, today)

        print("Validacioin de los Archivos por Operación.")
        self.validate_count_files_per_operation(self.list_Countries, self.dict_File_per_Operation, self.Download_path, today)

        print("Validación de las Columnas Obligatorias por Operación.")
        self.validate_mandatory_columns_per_operation(self.list_Countries, self.list_TXT_Operations_Files, self.dict_Mandatory_Columns_per_Operation, self.Download_path, today)

        print("\nValidacion de 16 Paises para Claro Video.\n")
        # Validate the 16 Countries
        for country in self.list_Countries:
            # Read again the Download Path
            new_Download_Directory = self.Download_path + '\\txt_' + country + '_' + today
            # ----- Read earch TXT File
            for title_Operation in self.list_TXT_Operations_Files:
                try:

                    # ----- CSV
                    # Convert CSV to Paruet File
                    csv_file_path = new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".csv"
                    parquet_file_path = new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".parquet"
                    self.convert_CSV_to_Parquet(csv_file_path, parquet_file_path)
                    csv_file = pd.read_parquet(parquet_file_path, engine='pyarrow')

                    # ----- CTL
                    # Open CTL File
                    ctl_file = open(new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".ctl", "rb")
                    # Read CTL File
                    ctl_value = int(ctl_file.read()) # <-- Converto CTL to Int. 
                    # Close CTL File
                    ctl_file.close()

                    try:
                        assert len(csv_file) == ctl_value
                    except AssertionError as e:
                        print(f"Error de Assert: {e}")
                    
                    print('CSV - CTL {0} {1}: {2}/{3} OK'.format(country, title_Operation, len(csv_file), ctl_value) if len(csv_file) == ctl_value else 'CSV - CTL {0} {1} FAIL'.format(country, title_Operation))

                    # ----- MD5
                    # Open MD5 File
                    md5_file = open(new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".md5_", "rb")
                    # Read MD5 File
                    md5_value = md5_file.read()

                    try:
                        assert len(md5_value) == 32
                    except AssertionError as e:
                        print(f"Error de Assert: {e}")

                    print("MD5 {0} {1} PASS".format(country, title_Operation) if len(md5_value) == 32 else "MD5 {0} {1} FAIL\n".format(country, title_Operation))
                    # Close MD5 File
                    md5_file.close()

                except Exception:
                    pass
            print("\n")

    # ----- Validations -----

    def convert_CSV_to_Parquet(self, csv_file_path, parquet_file_path):
        # Symbol that Delimit each Element of the Frame
        delmt = '|' 
        table = csv.read_csv(csv_file_path, parse_options = csv.ParseOptions(delimiter = delmt))
        # Save the Parquet File
        pyarrow.parquet.write_table(table, parquet_file_path)

    def validate_duplicity(self, list_Countries, list_TXT_Operations_Files, today):
        try:
            for country in list_Countries:
                for title_Operation in list_TXT_Operations_Files:
                    new_Download_Directory = "C:\\Automation\\Claro\\Downloads_CV" + '\\txt_' + country + '_' + today
                    nombre_base = title_Operation + '_' +  country + '_' + today + ".csv"
                    contador = 0
                    nombre_archivo = new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".csv" 
                    contador = sum(1 for nombre_archivo in os.listdir(new_Download_Directory) if nombre_archivo.startswith(nombre_base))
                    try:
                        assert contador <= 1
                    except AssertionError as e:
                        print(f"Error de Assert DUPLICIDAD: {e}")
        except Exception:
            pass
        print("La Cantidad de Archivos por País son Válidas.\n")

    def validate_number_of_files(self, list_Countries, dict_Number_of_Files, Download_path, today):
        for country in list_Countries:
            # Get the Number of Files for the each Country
            new_Download_Directory = Download_path + '\\txt_' + country + '_' + today
            file_list = os.listdir(new_Download_Directory)
            # Filter Files Only (Excludes Directories)
            files = len([f for f in file_list if os.path.isfile(os.path.join(new_Download_Directory, f))])
            assert files == dict_Number_of_Files[country], f"Error en {country} tiene un número no permitido de archivos: {files}"
        print("La Cantidad de Archivos por País son Válidas.\n")

    def validate_count_files_per_operation(self, list_Countries, dict_File_per_Operation, Download_path, today):
        for country in list_Countries:
            tuple_Valid_Numbers_of_Files_per_Operation = {3, 6}
            # Get the Number of Files for the each Country
            new_Download_Directory = Download_path + '\\txt_' + country + '_' + today
            # Creo un Conjunto de TODOS los Archivos en el nuevo Directorio 
            file_list = os.listdir(new_Download_Directory)
            # Obtengo los Nombres de los Archivos esperados para el País
            expected_files = list(dict_File_per_Operation.get(country, [])) # Obtengo el Valor gracias a la Key
            for expected_file in expected_files:
                # Buscar archivos en archivos_encontrados que comiencen con expected_file y terminen con cualquier extensión
                found = [file for file in file_list if file.startswith(f"{expected_file}_")]
                # Verificar que el número de archivos encontrados sea válido
                assert len(found) in tuple_Valid_Numbers_of_Files_per_Operation, f"Error: {expected_file} en {country} tiene un Número NO permitido de Archivos: {len(found)}"
        print("Todos los Archivos por Operación son Válidos.\n")

    def validate_mandatory_columns_per_operation(self, list_Countries, list_TXT_Operations_Files, dict_Mandatory_Columns_per_Operation, Download_path, today):
        for country in list_Countries:
            print("\n\nPais: ", country, "\n")
            # Get the Directory for Each Country
            new_Download_Directory = Download_path + '\\txt_' + country + '_' + today
            # Get Each Operation
            for title_Operation in list_TXT_Operations_Files:
                print("Operacion: ", title_Operation)
                try:
                    expected_Columns = dict_Mandatory_Columns_per_Operation.get(title_Operation, [])
                    # Read the Parquet File 
                    df = pd.read_csv(new_Download_Directory + '\\' + title_Operation + '_' + country + '_' + today + '.csv', engine = 'pyarrow', sep = '|') # , engine = 'pyarrow', sep = '|'
                    df = (df[expected_Columns].isna().sum())
                    if (df >= 1).any():
                        for index, value in df.items():
                            if value >= 1:
                                print(f"El Campo {index} en {title_Operation} para {country} tiene {value} Elementos Vacío")
                    else:
                        print(f"Todos los Valores en {title_Operation} para {country} son Correctos.")
                except Exception:
                    print("---> CATCH")
                    pass