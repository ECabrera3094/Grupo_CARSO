#import json
import time
from playwright.sync_api import Page

from Locators.locators_Engagement import Locators_Engagement

class Engagement:

    def __init__(self, page: Page):
        self.page = page
        self.URL = Locators_Engagement.URL
        self.email = Locators_Engagement.email
        self.variables = Locators_Engagement.variables

    def navigate(self):
        self.page.goto(self.URL)

    def engagement_ClaroVideo(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill('cv-welcome\ncv-passwordreminder\ncv-change-password-success\ncv-activatecontrolpin\ncv-remembercontrolpin\ncv-newlogin-notification')
        #self.page.locator("id=keys").fill('email_susc_telmexmexico_abono_universal_plus_uruguay_amcogate_0\nemail_susc_telmexmexico_abono_universal_plus_uruguay_hubgate_0\nemail_susc_telmexmexico_abono_universal_plus_uruguay_promogate_0\nemail_susc_telmexmexico_abono_universal_plus_uruguay_hubgate_0_70007061\nemail_cancel_telmexmexico_abono_universal_plus_uruguay_hubgate_1200\nemail_cancel_telmexmexico_abono_universal_plus_uruguay_amcogate_1200\nemail_cancel_telmexmexico_abono_universal_plus_uruguay_promogate_1200')

        self.page.locator("id=regions").fill("MX")
        #self.page.locator("id=regions").fill("UY")

        self.page.locator("id=partner").select_option("CLAROVIDEO")
        
        '''
        Convertir el diccionario a una cadena JSON con Comillas Dobles.
        La función json.dumps() en Python convierte un objeto de Python (como un diccionario) en una cadena de texto en formato JSON. 
        Al establecer ensure_ascii=False, indicas que los caracteres especiales deben mostrarse tal como están, sin convertirlos a secuencias de escape.
        '''
        #json_string_variables = json.dumps(self.variables, ensure_ascii=False)
        #self.page.locator("id=variables").fill(json_string_variables)

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)
        
        self.page.screenshot(path="ClaroVideo_screenshot03.png")

    def engagement_ClaroMusica(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill("cm-welcome-jwt")

        self.page.locator("id=regions").fill("MX")

        self.page.locator("id=partner").select_option("CLAROMUSICA")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroMusica_screenshot03.png")

    def engagement_ClaroDrive(self):
        
        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill("cb_welcome\ncd-recovery-password")

        self.page.locator("id=regions").fill("MX")

        self.page.locator("id=partner").select_option("CLARODRIVE")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroDrive_screenshot03.png")

    def engagement_ClaroConnect(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill("cc-emails-remember\ncc-emails-invite\ncc-emails-forgotpw\ncc-emails-cancel")

        self.page.locator("id=regions").fill("MX")

        self.page.locator("id=partner").select_option("CLAROCONNECT")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroConnect_screenshot03.png")