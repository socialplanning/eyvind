# Future plans:
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
from paste.response import header_value

from beaker.middleware import SessionMiddleware

import time
import base64

import hmac
import sha

from urllib import quote, unquote, urlencode
from Cookie import BaseCookie

from signedheaders import add_signed_header

from logging import error

from sys import exit

def get_secret(conf):
    try:
        secret_filename = conf['topp_secret_filename']
    except KeyError:
        error("topp_secret_filename not set.  Auth will fail.")
        exit(1) 
    f = open(secret_filename)
    secret = f.readline().strip()
    f.close()
    return secret

class _AuthenticationMiddleware(object):
    """
This middleware reads a cookie which is set by the Eyvind application,
and sets a signed REMOTE_USER header so that downstream applications
don't need to deal with authentication.
    """
    def __init__(self, app, app_conf):
        """
        The application configuration should contain
        topp_secret_filename (for now; this will change).
        """
        self.app = app
        self.secret = get_secret(app_conf)
        
    def authenticate(self, environ):
        """
        Authenticate a user from a request.
        """
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

        add_signed_header(environ, 'REMOTE_USER', username, self.secret)

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
        ## FIXME: this isn't well specified nor its semantics specified:
        ignore = header_value(headers, 'X-Eyvind-Handling') or ''
        if ignore.lower() == 'ignore':
            return False
        ## FIXME: why redirect 403?
        return status.startswith('401') or status.startswith('403')

    def __call__(self, environ, start_response):
        
        if environ['PATH_INFO'].strip("/").startswith("_debug"):
            return self.app(environ, start_response)

        #set up environ['REMOTE_USER']
        self.authenticate(environ)

        req_with = environ.get('HTTP_X_REQUESTED_WITH', '').lower()
        if req_with == 'xmlhttprequest':
            # Don't intercept output
            return self.app(environ, start_response)
        status, headers, body = intercept_output(environ, self.app, self.needs_redirection, start_response)
            
        if status and status.startswith("401"):
            url = construct_url(environ)
            location = '/auth/login?came_from=%s' % quote(url)
        else:
            location = "/?portal_status_message=You+have+insufficient+privileges."
            
        if status:
            status = "303 See Other"
            headers = [('Location', location), ('Content-Type', 'text/html')]
            start_response(status, headers)
            return []
        else:
            return body

def AuthenticationMiddleware(app, app_conf):
    return SessionMiddleware(_AuthenticationMiddleware(app, app_conf))

