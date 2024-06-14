import time
from playwright.sync_api import Page

from Locators.locators_Engagement import Locators_Engagement

class Engagement:

    def __init__(self, page: Page):
        self.page = page
        self.URL = Locators_Engagement.URL
        self.email = Locators_Engagement.email

    def navigate(self):
        self.page.goto(self.URL)

    def engagement_ClaroVideo(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.screenshot(path="ClaroVideo_screenshot01.png")

        self.page.locator("id=keys").fill('cv-welcome\ncv-passwordreminder\ncv-change-password-success\ncv-activatecontrolpin\ncv-remembercontrolpin\ncv-newlogin-notification')

        self.page.locator("id=regions").fill("MX")

        self.page.locator("id=partner").select_option("CLAROVIDEO")

        self.page.screenshot(path="ClaroVideo_screenshot02.png")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroVideo_screenshot03.png")

    def engagement_ClaroMusica(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.screenshot(path="ClaroMusica_screenshot01.png")

        self.page.locator("id=keys").fill("cm-welcome-jwt")

        self.page.locator("id=regions").fill("MX")

        self.page.locator("id=partner").select_option("CLAROMUSICA")

        self.page.screenshot(path="ClaroMusica_screenshot02.png")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroMusica_screenshot03.png")

    def engagement_ClaroDrive(self):
        
        self.page.locator("id=emails").fill(self.email)

        self.page.screenshot(path="ClaroDrive_screenshot01.png")

        self.page.locator("id=keys").fill("cb_welcome-wsgu\ncd-recovery-password")

        self.page.locator("id=regions").fill("MX")

        self.page.locator("id=partner").select_option("CLARODRIVE")

        self.page.screenshot(path="ClaroDrive_screenshot02.png")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroDrive_screenshot03.png")

    def engagement_ClaroConnect(self):

        self.page.locator("id=emails").fill(self.email)

        self.page.screenshot(path="ClaroConnect_screenshot01.png")

        self.page.locator("id=keys").fill("cc-emails-remember\ncc-emails-invite\ncc-emails-forgotpw\ncc-emails-cancel")

        self.page.locator("id=regions").fill("MX")

        self.page.locator("id=partner").select_option("CLAROCONNECT")

        self.page.screenshot(path="ClaroConnect_screenshot02.png")

        time.sleep(3)

        self.page.locator("id=sender").click(force = True)

        time.sleep(10)

        self.page.screenshot(path="ClaroConnect_screenshot03.png")