from pages.secure_area_page import SecureAreaPageLocators
import pytest


class SecureAreaActions(SecureAreaPageLocators):

    def __init__(self, app):
        self.app = app

    def get_secure_area_title(self):
        driver = self.app.driver
        return driver.find_element(*SecureAreaPageLocators.TITLE_AREA).text

    def check_secure_area_text(self, area):
        with pytest.allure.step('Verify sub-header text for Secure area page'):
            return self.get_secure_area_title() == area
