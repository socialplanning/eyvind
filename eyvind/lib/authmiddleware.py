# Eyvind authentication middleware.  Eyvind checks TeamRoller's
# database to determine if a user can log in.

# Sessions:
# Users have only a session id, which is randomly generated
# The secret disappears
# Logging out destroys the session.
# The session (usually) expires.
# The session is locked to a subnet.
# The session contains the username
# Where are sessions stored?  

# Copyright (C) 2006-2007 The Open Planning Project

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the 
# Free Software Foundation, Inc., 
# 51 Franklin Street, Fifth Floor, 
# Boston, MA  02110-1301
# USA


from paste.wsgilib import intercept_output
from paste.request import construct_url

from beaker.session import SessionMiddleware

import time
import base64

import hmac
import sha

from urllib import quote, unquote, urlencode
from Cookie import BaseCookie

def get_secret(conf):
    secret_filename = conf['topp_secret_filename']
    f = open(secret_filename)
    secret = f.readline().strip()
    f.close()
    return secret

class _AuthenticationMiddleware(object):
    def __init__(self, app, app_conf):
        self.app = app
        self.secret = get_secret(app_conf)
        
    def authenticate(self, environ):
        try:
            cookie = BaseCookie(environ['HTTP_COOKIE'])
            morsel = cookie['__ac']
        except KeyError:
            return False

        try:
            username, auth = base64.decodestring(unquote(morsel.value)).split("\0")

        except ValueError:
            raise BadCookieError

        if not auth == hmac.new(self.secret, username, sha).hexdigest():
            return False

        environ['REMOTE_USER'] = username
        environ['HTTP_X_OPENPLANS_USERNAME'] = username

#         session = environ['beaker.session']
#         if not 'username' in session:
#             return False

#         #manually expire session
#         if session['expiration']:
#             now = time.time()
#             if session['expiration'] > now:
#                 session.invalidate()
#                 return False
#             session['expiration'] = now + (60 * 60 * 8)
                

#         username = session['username']

#         session.save()


        
    def needs_redirection(self, status, headers):
        return status.startswith('401') or status.startswith('403')

    def __call__(self, environ, start_response):
        
        if environ['PATH_INFO'].strip("/").startswith("_debug"):
            return self.app(environ, start_response)

        #set up environ['REMOTE_USER']
        self.authenticate(environ)

        status, headers, body = intercept_output(environ, self.app, self.needs_redirection, start_response)

        if status and status.startswith("401"):
            location = '"/login"?came_from=%s' % (location, quote(url))
        else:
            location = "/"
            
        if status:
            status = "303 See Other"
            url = construct_url(environ)
            headers = [('Location', location), ('Content-Type', 'text/html')]
            start_response(status, headers)
            return []
        else:
            return body

def AuthenticationMiddleware(app, app_conf):
    return SessionMiddleware(_AuthenticationMiddleware(app, app_conf))

