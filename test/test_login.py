import pytest


######################################
# Test page "Secure Area" #
######################################

def test_login(app, config):
    app.login_page.enter_login_information(config['web']['username'], config['web']['password'])
    assert app.secure_area_page.check_secure_area_text(
        'Welcome to the Secure Area. When you are done click logout below.'), \
        "Text could not be found on the Secure Area page"
