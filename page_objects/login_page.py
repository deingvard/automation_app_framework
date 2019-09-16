from selenium.webdriver.common.by import By


class PageLocators(object):
    USER_NAME_INPUT = (By.NAME, "username")
    USER_PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


class LoginPage(PageLocators):

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(*PageLocators.USER_NAME_INPUT).click()
        wd.find_element(*PageLocators.USER_NAME_INPUT).clear()
        wd.find_element(*PageLocators.USER_NAME_INPUT).send_keys(username)
        wd.find_element(*PageLocators.USER_PASSWORD_INPUT).click()
        wd.find_element(*PageLocators.USER_PASSWORD_INPUT).clear()
        wd.find_element(*PageLocators.USER_PASSWORD_INPUT).send_keys(password)
        wd.find_element(*PageLocators.SUBMIT_BUTTON).click()

