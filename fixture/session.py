

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name('username').clear()
        wd.find_element_by_name('username').send_keys(username)

        wd.find_element_by_name("password").click()
        wd.find_element_by_name('password').clear()
        wd.find_element_by_name('password').send_keys(password)

        wd.find_element_by_css_selector('button[type="submit"]')


