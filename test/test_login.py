import time


def test_login(app):
    app.session.login("tomsmith", "SuperSecretPassword!")
    app.session.is_logged_in()
    assert app.session.is_logged_in_as('You logged into a secure area!')# == 'You logged into a secure area!', 'Fail'
    time.sleep(5)
    app.session.logout()


