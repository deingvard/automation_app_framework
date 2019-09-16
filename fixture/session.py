from selenium.webdriver.common.by import By


class PageLocators(object):
    USER_NAME_INPUT = (By.NAME, "username")
    USER_PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')
    LOGGED_AREA = (By.CLASS_NAME, 'subheader')


class SessionHelper(PageLocators):

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

    def logout(self):
        wd = self.app.wd
        wd.find_element(*PageLocators.LOGOUT_BUTTON).click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(*PageLocators.LOGOUT_BUTTON)) > 0

    def is_logged_in_as(self, area):
        return self.get_logged_are() == area

    def get_logged_are(self):
        wd = self.app.wd
        return wd.find_element(*PageLocators.LOGGED_AREA).text
