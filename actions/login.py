from pages.login_page import LoginPageLocators
import pytest


class LoginActions(LoginPageLocators):

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.login_actions = LoginPageLocators(driver=self.driver)

    """ Enter username, string value"""
    def enter_username(self, username):
        with pytest.allure.step('Enter username'):
            self.login_actions.user_name_input.click()
            self.login_actions.user_name_input.clear()
            self.login_actions.user_name_input.send_keys(username)

    """ Enter password, string value"""
    def enter_password(self, password):
        with pytest.allure.step('Enter password'):
            self.login_actions.user_password_input.click()
            self.login_actions.user_password_input.clear()
            self.login_actions.user_password_input.send_keys(password)

    """ Click Submit button"""
    def click_submit_button(self):
        with pytest.allure.step('Click submit button'):
            self.login_actions.submit_button.click()
