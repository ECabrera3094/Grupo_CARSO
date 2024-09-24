class Locators_validation_TXT_CV():

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

    list_TXT_Operations_Files = ['Catalogo',
                    'Suscripciones',
                    'SuscripcionesDiarias',
                    'Temporada',
                    'Transacciones',
                    'Usuarios',
                    'Usuarios_Eliminados',
                    'UsuariosInactivos',
                    'UsuariosSinCustomerId',
                    'Visualizaciones']

    dict_Number_of_Files = {
                    'ARGENTINA' : 27,
                    'BRASIL' : 21,
                    'CHILE' : 27,
                    'COLOMBIA' : 27,
                    'COSTARICA' : 27,
                    'DOMINICANA' : 27,
                    'ECUADOR' : 27,
                    'ELSALVADOR' : 27,
                    'GUATEMALA' : 27,
                    'HONDURAS' : 27,
                    'MEXICO' : 24,
                    'NICARAGUA' : 27,
                    'PANAMA' : 27,
                    'PARAGUAY' : 27,
                    'PERU' : 27,
                    #'PUERTORICO' : 27, # <-----
                    'URUGUAY' : 21
                    }
					
    dict_File_per_Operation = {
                        'ARGENTINA' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'BRASIL' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados','Visualizaciones'],
                        'MEXICO' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Temporada', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados','Visualizaciones'],
                        'CHILE' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'COLOMBIA' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'COSTARICA' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'DOMINICANA' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'ECUADOR' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones', 'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'ELSALVADOR' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'GUATEMALA' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'HONDURAS' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'NICARAGUA' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'PANAMA' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'PARAGUAY' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'PERU' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'UsuariosInactivos', 'UsuariosSinCustomerId', 'Visualizaciones'],
                        'URUGUAY' : ['Catalogo', 'Suscripciones', 'SuscripcionesDiarias', 'Transacciones',  'Usuarios', 'Usuarios_Eliminados', 'Visualizaciones']
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
    # 14
    #xpath_descargar_archivo_button = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[3]/div[4]/div/span/div/div/span/span/a/button"

    Drivers_path = "C:\\Automation\\Claro\\Drivers\\chromedriver.exe"
    Download_path = "C:\\Automation\\Claro\\Downloads_CV"