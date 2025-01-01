class locator():

    Loocker_URL = "https://amco.cloud.looker.com/login"
    textbox_user = "login-email"
    id_textbox_password = "login-password"
    boton_acceder = "login-submit"
    Loocker_user = "datos_qa.cmx@clarovideotv.com"
    Loocker_password = "89Fu8B;48:0Y"
    xpath_dashboard_claro_video_link = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/a/span"
    xpath_production_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[1]/div/div[1]/lk-breadcrumbs/div/ul/li[2]/a"
    xpath_reportes_homologados = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[5]/div/div"
    xpath_claro_video = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[3]/div/div"
    xpath_finanzas = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[9]/div/div"
    xpath_archivos_CVMAX = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-folder-children-section/div/div[2]/a[4]/div/div"
    xpath_archivos_operaciones_CVMAX = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[2]/div/div/lk-browse-table[1]/table/tbody/tr/td[3]/div/a/div[1]"
    xpath_descarga_archivo = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/span/div/div/span/span/a/button"
    xpath_confirmación_de_reporte ='/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[1]/h1'
    xpath_reportesDisponibles = '/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/div/button/div[1]'
    #Localizador de drive y descompresion
    Drivers_path = "C:\\Auto_amco\\drivers\\chromedriver.exe"
    Download_path = "C:\\Auto_amco\\reportes\\Semanal_CVMAX"

    #Asserts
    camino_prod = '/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[1]/div/div[1]/lk-breadcrumbs/div/ul/li[2]/h2'

