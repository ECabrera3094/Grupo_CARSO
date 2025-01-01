class Locators_validation_TXT_LOGIN():
    
    Loocker_URL = "https://amco.cloud.looker.com/login"
    Loocker_URL_Archivos_Operaciones_LOGIN = "https://amco.cloud.looker.com/dashboards/814"
    Loocker_user = "datos_qa.cmx@clarovideotv.com"
    Loocker_password = "89Fu8B;48:0Y"
    list_Countries = ['ARGENTINA',
                    'BRASIL',
                    'CHILE',
                    'COLOMBIA',
                    'COSTARICA',
                    'DOMINICANA',
                    'ECUADOR',
                    'ELSALVADOR',
                    'GUATEMALA',
                    'HONDURAS',
                    'MEXICO',
                    'NICARAGUA',
                    'PANAMA',
                    'PARAGUAY',
                    'PERU',
                    'URUGUAY']

    list_TXT_Operations_Files = ['registro']

    dict_Number_of_Files = {
                    'ARGENTINA' : 3,
                    'BRASIL' : 3,
                    'CHILE' : 3,
                    'COLOMBIA' : 3,
                    'COSTARICA' : 3,
                    'DOMINICANA' : 3,
                    'ECUADOR' : 3,
                    'ELSALVADOR' : 3,
                    'GUATEMALA' : 3,
                    'HONDURAS' : 3,
                    'MEXICO' : 3,
                    'NICARAGUA' : 3,
                    'PANAMA' : 3,
                    'PARAGUAY' : 3,
                    'PERU' : 3,
                    'URUGUAY' : 3
                    }

    dict_File_per_Operation = {
                    'ARGENTINA' : ['registro'],
                    'BRASIL' : ['registro'],
                    'MEXICO' : ['registro'],
                    'CHILE' : ['registro'],
                    'COLOMBIA' : ['registro'],
                    'COSTARICA' : ['registro'],
                    'DOMINICANA' : ['registro'],
                    'ECUADOR' : ['registro'],
                    'ELSALVADOR' : ['registro'],
                    'GUATEMALA' : ['registro'],
                    'HONDURAS' : ['registro'],
                    'NICARAGUA' : ['registro'],
                    'PANAMA' : ['registro'],
                    'PARAGUAY' : ['registro'],
                    'PERU' : ['registro'],
                    'URUGUAY' : ['registro']
                    }

    dict_Mandatory_Columns_per_Operation = {
                    'registro': ["FECHA", "TXT_CATEGORIA_DISPOSITIVO", "TX_FABRICANTE_DISPOSITIVO", "TX_MODELO_DISPOSITIVO", "TX_SO_DISPOSITIVO", "EMAIL", "PAIS", "MSG", "TYC", "NOMBRE", "APELLIDO", "ID_CLIENTE", "IP_ORIGEN", "PORT", "TIPO_EVENTO", "CODIGO_ERROR", "DESCRIPCION_ERROR", "TELEFONO"]
                    }

    id_textbox_user = "login-email"
    id_textbox_password = "login-password"
    id_loging_button = "login-submit"
    xpath_main_page_logo = "/html/body/div[2]/div/div/div/header/div/div[1]/a/div/svg"
    xpath_dashboard_claro_video_link = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/a/span"
    xpath_produccion_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[1]/div/div[1]/lk-breadcrumbs/div/ul/li[2]/a"
    xpath_reportes_homologados_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[5]/div/div"
    xpath_claro_video_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[3]/div/div"
    xpath_archivos_txt_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[2]/div/div"
    xpath_archivos_operaciones_cv_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-browse-table[1]/table/tbody/tr[1]/td[3]/div/a/div[1]"
    xpath_pais_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div/div/span/span"
    xpath_close_pais = "/html/body/div[3]/div/div/div/div/div/div/div/div/div[2]/button/div[2]"
    xpath_listbox_pais = "/html/body/div[3]/div/div/div/div/div/div/div/div/div[1]/input[2]"
    xpath_actualizar_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/div/button"                
    xpath_panel_actions = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/button[2]/div[2]" #/svg
    xpath_clear_cache_update = "/html/body/div[3]/div/div/div/div/div/ul/li[1]/button/div[2]/span"
    xpath_descargar_archivo_button = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/span/div/div/span/span/a/button"
    #xpath_descargar_archivo_button ="/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[3]/div[4]/div/span/div/div/span/span/a/button"


    Drivers_path = "C:\\Automation\\Claro\\Drivers\\chromedriver.exe"
    Download_path = "C:\\Automation\\Claro\\Downloads_LOGIN"