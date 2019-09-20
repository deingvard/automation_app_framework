######################################
# Test page "Secure Area" #
######################################

def test_login(app, config):
    app.open_home_page()
    app.login_page.enter_username(config['web']['username'])
    app.login_page.enter_password(config['web']['password'])
    app.login_page.click_submit_button()
    assert app.secure_area_page.check_secure_area_text(
        'Welcome to the Secure Area. When you are done click logout below.'), \
        "Text could not be found on the Secure Area page"
