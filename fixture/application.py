from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        # Set browser
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path='/Users/admin/Downloads/chromedriver')
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
        self.session = SessionHelper(self)
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
