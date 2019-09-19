from selenium.webdriver.common.by import By
import pytest


class PageLocators(object):
    TITLE_AREA = (By.CLASS_NAME, 'subheader')


class SecureAreaPage(PageLocators):

    def __init__(self, app):
        self.app = app

    def get_secure_area_title(self):
        driver = self.app.driver
        return driver.find_element(*PageLocators.TITLE_AREA).text

    def check_secure_area_text(self, area):
        with pytest.allure.step('Verify sub-header text for Secure area page'):
            return self.get_secure_area_title() == area
