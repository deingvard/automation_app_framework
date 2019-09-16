import pytest


######################################
# Test page "Secure Area" #
######################################

def test_login(app, config):
    with pytest.allure.step('Open Login Page and fill in fields "Username" and "Password", click "Login'):
        app.login_page.enter_login_information(config['web']['username'], config['web']['password'])
    with pytest.allure.step('Verify sub-header text for "Secure area" page'):
        assert app.secure_area_page.check_secure_area_text(
            'Welcome to the Secure Area. When you are done click logout below.')
    with pytest.allure.step('Click "Logout" button'):
        app.secure_area_page.click_logout_button()
