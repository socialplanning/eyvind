import paste

from eyvind.lib.authmiddleware import AuthenticationMiddleware

import os

secret_filename = os.path.join(os.path.dirname(__file__), 'secret')

def un_app(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return ["Username = %s" % environ.get('HTTP_X_OPENPLANS_USERNAME', '0')]

def test_auth_middleware():
    app = AuthenticationMiddleware(un_app, {'topp_secret_filename' : secret_filename})
    app = paste.fixture.TestApp(app)
    res = app.get("/")
    assert res.body == "Username = 0"
    extra_environ = {'HTTP_COOKIE' : '__ac="ZGFyY2lhAGI1NDM2MDg2ZGQ3NGYxMmYzZDEzNDQzMjlhYmVlMTE3NTM3NGY1ODA%3D%0A"'
                     }


    res = app.get("/", extra_environ=extra_environ)
    assert res.body == "Username = darcia"

