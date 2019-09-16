from selenium.webdriver.common.by import By


class PageLocators(object):
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')
    TITLE_AREA = (By.CLASS_NAME, 'subheader')


class SecureAreaPage(PageLocators):

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element(*PageLocators.LOGOUT_BUTTON).click()

    def is_logged_in_as(self, area):
        return self.get_logged_are() == area

    def get_logged_are(self):
        wd = self.app.wd
        return wd.find_element(*PageLocators.TITLE_AREA).text
