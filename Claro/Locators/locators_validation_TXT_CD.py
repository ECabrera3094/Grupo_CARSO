class Locators_validation_TXT_CD():

    Loocker_URL = "https://amco.cloud.looker.com/login"
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

    list_TXT_Operations_Files = ['Consumos',
                    'Consumos_Pyme',
                    'Estado_Medio_Pago',
                    'Suscripciones',
                    'Usuarios',
                    'Usuarios_Eliminados'
                    ]

    id_textbox_user = "login-email"
    id_textbox_password = "login-password"
    id_loging_button = "login-submit"
    xpath_main_page_logo = "/html/body/div[2]/div/div/div/header/div/div[1]/a/div/svg"
    xpath_dashboard_claro_video_link = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/a/span"
    xpath_produccion_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[1]/div/div[1]/lk-breadcrumbs/div/ul/li[2]/a"
    xpath_reportes_homologados_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[5]/div/div"
    xpath_claro_drive_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[1]/div/div"                     
    xpath_claro_drive_masivo = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[1]/div/div"                             
    xpath_archivos_txt_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[1]/div/div"                           
    xpath_archivos_operaciones_cd_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-browse-table[1]/table/tbody/tr/td[3]/div/a/div[1]"
    xpath_pais_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div/div/span/span"
    xpath_close_pais = "/html/body/div[3]/div/div/div/div/div/div/div/div/div[2]/button/div[2]"
    xpath_listbox_pais = "/html/body/div[3]/div/div/div/div/div/div/div/div/div[1]/input[2]"
    xpath_actualizar_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/div/button"                
    xpath_panel_actions = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/button[2]/div[2]" #/svg
    
    xpath_clear_cache_update = "/html/body/div[3]/div/div/div/div/div/ul/li[1]/button/div[2]/span"
    
    
    
    
    xpath_descargar_archivo_button = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/span/div/div/span/span/a/button"

    Drivers_path = "C:\\Automation\\Claro\\Drivers\\chromedriver.exe"
    Download_path = "C:\\Automation\\Claro\\Downloads_CD"