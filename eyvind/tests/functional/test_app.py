from eyvind.tests import *
import re
from wsgi_intercept import add_wsgi_intercept, httplib2_intercept

import paste

class TestApp(TestController):
    def __init__(self, test):
        TestController.__init__(self, test)

    def test_login(self):
        #assume a user named test, password testy

        #set up HTTP mocks
        httplib2_intercept.install()
        add_wsgi_intercept('testopenplans.example.com', 80, LoginServer)

        res = self.app.get("/login")
        #try a good login

        form = res.forms[0]
        form['username'] = 'test'
        form['password'] = 'testy'
        res = form.submit()
        
        assert '/people/test/account' in res.header_dict['location']
        assert '?portal_status_message=Welcome' in res.header_dict['location']
        
        #now one with came_from

        res = self.app.get("/login")
        #try a good login

        form = res.forms[0]
        form['username'] = 'test'
        form['password'] = 'testy'
        form['came_from'] = '/camefrom'
        res = form.submit()
        
        assert res.header_dict['location'].startswith('/camefrom?portal_status_message=Welcome')

        #now a failure

        res = self.app.get("/login")
        #try a good login

        form = res.forms[0]
        form['username'] = 'test'
        form['password'] = 'wrong'
        form['came_from'] = '/camefrom'

        res = form.submit()

        form = res.forms[0]
        assert form['came_from'].value == '/camefrom'
        #res.mustcontain('Please check your username and password')
        assert 'Please check your username and password' in res


class LoginServer:
    def __init__(self):
        pass

    def clear(self):
        pass

    def __call__(self, environ, start_response):
        path_info = environ.get('PATH_INFO', '')
        req = paste.wsgiwrappers.WSGIRequest(environ)

        assert environ['PATH_INFO'] == '/people/test/get-hash'
        assert environ['REQUEST_METHOD'] == "POST"

        password = environ['wsgi.input'].read()
        start_response('200 OK', [])

        if password == "__ac_password=testy":
            return ['__ac=agoodcookie']
        else:
            return ['']            
