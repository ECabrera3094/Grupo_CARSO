from playwright.sync_api import Page

from TestCases.test_engagement import Engagement

def test_basic_search(page: Page):

    send_email = Engagement(page)
    send_email.navigate()
    send_email.engagement_ClaroVideo()
    send_email.engagement_ClaroMusica()
    send_email.engagement_ClaroDrive()
    send_email.engagement_ClaroConnect()

# python -m pytest test_main.py