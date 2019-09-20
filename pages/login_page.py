from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USER_NAME_INPUT = (By.NAME, "username")
    USER_PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

