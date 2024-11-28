import json
import time
from playwright.sync_api import Page

from Locators.locators_Engagement import Locators_Engagement

class Engagement:

    def __init__(self, page: Page):
        self.page = page
        self.URL = Locators_Engagement.URL
        self.email = Locators_Engagement.email
        self.keys_ClaroVideo = Locators_Engagement.keys_ClaroVideo
        self.keys_ClaroMusic = Locators_Engagement.keys_ClaroMusic
        self.Keys_ClaroDrive = Locators_Engagement.Keys_ClaroDrive
        self.keys_ClaroConnect = Locators_Engagement.keys_ClaroConnect
        self.region = Locators_Engagement.region
        self.variables = Locators_Engagement.variables

    def navigate(self):
        self.page.goto(self.URL)

    def engagement_ClaroVideo(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill(self.keys_ClaroVideo)
        
        self.page.locator("id=regions").fill(self.region)

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
        
        self.page.screenshot(path="ClaroVideo.png")

    def engagement_ClaroMusica(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill(self.keys_ClaroMusic)

        self.page.locator("id=regions").fill(self.region)

        self.page.locator("id=partner").select_option("CLAROMUSICA")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroMusica.png")

    def engagement_ClaroDrive(self):
        
        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill(self.Keys_ClaroDrive)

        self.page.locator("id=regions").fill(self.region)

        self.page.locator("id=partner").select_option("CLARODRIVE")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroDrive.png")

    def engagement_ClaroConnect(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.locator("id=keys").fill(self.keys_ClaroConnect)

        self.page.locator("id=regions").fill(self.region)

        self.page.locator("id=partner").select_option("CLAROCONNECT")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroConnect.png")