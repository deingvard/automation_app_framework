from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.secure_area_page import SecureAreaPage
import os


class Application:

    def __init__(self, browser, base_url):
        # Set browser
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            self.wd = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path=os.getcwd() + os.sep + os.sep + "libs/chromedriver")
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # Sets a sticky timeout to implicitly wait for an element to be found
        self.wd.implicitly_wait(5)
        # Invokes the window manager-specific 'full screen' operation
        self.wd.set_window_size(1980, 1020)
        # Delete all cookies in the scope of the session
        self.wd.delete_all_cookies()
        # Initialize pages
        self.login_page = LoginPage(self)
        self.secure_area_page = SecureAreaPage(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        # Stop the browser
        self.wd.quit()
