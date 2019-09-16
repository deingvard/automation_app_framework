import pytest


######################################
# Test page "Secure Area" #
######################################

def test_login(app, config):
    with pytest.allure.step('Open Login page and fill in login and password'):
        app.session.login(config['web']['username'], config['web']['password'])
    with pytest.allure.step('Verify Logout button on the page'):
        app.session.is_logged_in()
    with pytest.allure.step('Verify "Secure area" text on the page'):
        assert app.session.is_logged_in_as('Welcome to the Secure Area. When you are done click logout below.')
    with pytest.allure.step('Click button logout'):
        app.session.logout()
