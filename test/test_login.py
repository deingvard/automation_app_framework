
def test_login(app):
    app.session.login("tomsmith", "SuperSecretPassword!x")
