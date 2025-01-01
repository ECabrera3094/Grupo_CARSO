class Locators_validation_TXT_CD():

    Loocker_URL = "https://amco.cloud.looker.com/login"
    Loocker_URL_Archivos_Operaciones_CD = "https://amco.cloud.looker.com/dashboards/506"
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
                    'PUERTORICO',
                    'URUGUAY']

    list_TXT_Operations_Files = ['Consumos',
                    'Consumos_Pyme',
                    'Estado_Medio_Pago',
                    'Suscripciones',
                    'Usuarios',
                    'Usuarios_Eliminados'
                    ]

    dict_Number_of_Files = {
                    'ARGENTINA' : 15,
                    'BRASIL' : 15,
                    'CHILE' : 15,
                    'COLOMBIA' : 15,
                    'COSTARICA' : 15,
                    'DOMINICANA' : 15,
                    'ECUADOR' : 15,
                    'ELSALVADOR' : 15,
                    'GUATEMALA' : 15,
                    'HONDURAS' : 15,
                    'MEXICO' : 18,
                    'NICARAGUA' : 15,
                    'PANAMA' : 15,
                    'PARAGUAY' : 15,
                    'PERU' : 15,
                    'PUERTORICO' : 15,
                    'URUGUAY' : 15
                    }

    dict_File_per_Operation = {
                    'ARGENTINA' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'BRASIL' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'MEXICO' : ['Consumos', 'Consumos_Pyme','Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'CHILE' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'COLOMBIA' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'COSTARICA' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'DOMINICANA' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'ECUADOR' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'ELSALVADOR' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'GUATEMALA' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'HONDURAS' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'NICARAGUA' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'PANAMA' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'PARAGUAY' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'PERU' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'PUERTORICO' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados'],
                    'URUGUAY' : ['Consumos', 'Estado_Medio_Pago', 'Suscripciones', 'Usuarios', 'Usuarios_Eliminados']
                }

    dict_Mandatory_Columns_per_Operation = {
                    'Consumo' : ['PAIS','ID_CLIENTE','FECHA_EXTRACCION','ESPACIO_ASIGNADO','ESPACIO_CONSUMIDO','NRO_ARCHIVOS_BUZON','NRO_ARCHIVOS_COMPARTIDOS','NRO_ARCHIVOS_CREADOS','NROS_ARCHIVOS_LEIDOS','NOMBRE_SO'],
                    'Estado_Medio_Pago': ['PAIS','ID_CLIENTE','MSISDN','FECHA_ALTA','MEDIO_PAGO_NOMBRE','COD_ORIGEN_PAGO','TX_ORIGEN_PAGO','PAQUETE','ESTADO_MEDIO_PAGO'],
                    # Para el caso de MX, adicionalmente se debe realizar la siguiente validación:
                    # Filtrar desde el campo MEDIO_PAGO_NOMBRE por "Recibo Telmex" y verificar que el campo PRODUCTO_ID, no venga vacío y que todos los nombres finalicen con "CL"
                    'Suscripciones' : ["PAIS", "ID_CLIENTE","COD_PARTNER_OPERACION",'COD_FECHA_SUSC_PAIS','PRECIO','ABONO','TX_SUSCRIPCION','MEDIO_PAGO_NOMBRE','TX_CUENTA','COD_ORIGEN_PAGO','TX_ORIGEN_PAGO','COD_ORIGEN_ACCION','TX_ACCION','CANT_RENOVACIONES','USUARIO_ALTA','PAQUETE'],
                    'Usuarios' : ['PAIS','ID_CLIENTE','NOMBRE_COMPLETO','TX_MAIL','COD_FECHA_ALTA','COD_FECHA_TERM_ACEPT','COD_ORIGEN_ALTA','TX_ORIGEN_ALTA','USUARIO_ALTA','ID_ADMIN'],
                    'Usuarios_Eliminados' : ['ID_CLIENTE','NOMBRE_COMPLETO','TX_MAIL','COD_FECHA_ALTA','COD_FECHA_TERM_ACEPT','COD_ORIGEN_ALTA','TX_ORIGEN_ALTA','USUARIO_ALTA','COD_FECHA_BAJA']
                    }

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
    #xpath_descargar_archivo_button = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/span/div/div/span/span/a/button"

    Drivers_path = "C:\\Automation\\Claro\\Drivers\\chromedriver.exe"
    Download_path = "C:\\Automation\\Claro\\Downloads_CD"