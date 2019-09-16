import pytest


######################################
# Test page "Secure Area" #
######################################

def test_login(app, config):
    with pytest.allure.step('Open Login page and fill in login and password'):
        app.login_page.login(config['web']['username'], config['web']['password'])
    with pytest.allure.step('Verify "Secure area" text on the page'):
        assert app.secure_area_page.is_logged_in_as('Welcome to the Secure Area. When you are done click logout below.')
    with pytest.allure.step('Click button logout'):
        app.secure_area_page.logout()
