from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find


class SecureAreaPageLocators(BasePage):
    title_area = Find(by=By.CLASS_NAME, value="subheader")


