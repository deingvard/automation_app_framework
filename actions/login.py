from pages.login_page import LoginPageLocators
import pytest


class LoginActions(LoginPageLocators):

    def __init__(self, app):
        self.app = app

    def enter_login_information(self, username, password):
        with pytest.allure.step('Fill in fields "Username" and "Password", click "Login'):
            driver = self.app.driver
            driver.find_element(*LoginPageLocators.USER_NAME_INPUT).click()
            driver.find_element(*LoginPageLocators.USER_NAME_INPUT).clear()
            driver.find_element(*LoginPageLocators.USER_NAME_INPUT).send_keys(username)
            driver.find_element(*LoginPageLocators.USER_PASSWORD_INPUT).click()
            driver.find_element(*LoginPageLocators.USER_PASSWORD_INPUT).clear()
            driver.find_element(*LoginPageLocators.USER_PASSWORD_INPUT).send_keys(password)

    def click_submit_button(self):
        with pytest.allure.step('Click submit button'):
            driver = self.app.driver
            driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
