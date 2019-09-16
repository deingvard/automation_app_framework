from selenium.webdriver.common.by import By


class PageLocators(object):
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')
    TITLE_AREA = (By.CLASS_NAME, 'subheader')


class SecureAreaPage(PageLocators):

    def __init__(self, app):
        self.app = app

    def get_secure_area_title(self):
        wd = self.app.wd
        return wd.find_element(*PageLocators.TITLE_AREA).text

    def check_secure_area_text(self, area):
        return self.get_secure_area_title() == area

    def click_logout_button(self):
        wd = self.app.wd
        wd.find_element(*PageLocators.LOGOUT_BUTTON).click()
