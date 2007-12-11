import os
import paste
import urllib

from eyvind.lib.authmiddleware import AuthenticationMiddleware, get_secret
from signedheaders import HeaderSignatureCheckingMiddleware

secret_filename = os.path.join(os.path.dirname(__file__), 'secret')
conf = {'topp_secret_filename' : secret_filename}
secret = get_secret(conf)

def un_app(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return ["Username = %s" % environ.get('REMOTE_USER', '0')]

def get_app():
    app = HeaderSignatureCheckingMiddleware(un_app, secret)
    app = AuthenticationMiddleware(app, conf)
    app = paste.fixture.TestApp(app)
    return app

def test_auth_middleware():
    app = get_app()
    res = app.get("/")
    assert res.body == "Username = 0"
    extra_environ = {'HTTP_COOKIE' : 
                     '__ac="ZGFyY2lhAGI1NDM2MDg2ZGQ3NGYxMmYzZDEzNDQzMjlhYmVlMTE3NTM3NGY1ODA%3D%0A"'
                     }

    res = app.get("/", extra_environ=extra_environ)
    assert res.body == "Username = darcia"

def test_bad_auth():
    app = get_app()

    badcookie = urllib.quote("darcia\x00badcookie".encode("base64"))

    extra_environ = {'HTTP_COOKIE' : '__ac="%s"' % badcookie}

    res = app.get("/", extra_environ=extra_environ)
    assert res.body == "Username = 0"
