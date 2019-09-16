def test_login(app):
    app.session.login("tomsmith", "SuperSecretPassword!")
    app.session.is_logged_in()
    assert app.session.is_logged_in_as('Welcome to the Secure Area. When you are done click logout below.')
    app.session.logout()
