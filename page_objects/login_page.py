from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find
import pytest


class PageLocators(object):
    USER_NAME_INPUT = (By.NAME, "username")
    USER_PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


class LoginPage(PageLocators, BasePage):

    def __init__(self, app):
        self.app = app

    def enter_login_information(self, username, password):
        with pytest.allure.step('Open Login Page and fill in fields "Username" and "Password", click "Login'):
            driver = self.app.driver
            self.app.open_home_page()
            driver.find_element(*PageLocators.USER_NAME_INPUT).click()
            driver.find_element(*PageLocators.USER_NAME_INPUT).clear()
            driver.find_element(*PageLocators.USER_NAME_INPUT).send_keys(username)
            driver.find_element(*PageLocators.USER_PASSWORD_INPUT).click()
            driver.find_element(*PageLocators.USER_PASSWORD_INPUT).clear()
            driver.find_element(*PageLocators.USER_PASSWORD_INPUT).send_keys(password)
            driver.find_element(*PageLocators.SUBMIT_BUTTON).click()
