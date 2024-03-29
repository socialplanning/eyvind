"""The base Controller API

Provides the BaseController class for subclassing, and other objects
utilized by Controllers.
"""
from pylons import c, cache, config, g, request, response, session
from pylons.controllers import WSGIController
from pylons.controllers.util import abort, etag_cache, redirect_to
from pylons.decorators import jsonify, validate
from pylons.i18n import _, ungettext, N_
from pylons.templating import render

import eyvind.lib.helpers as h
import eyvind.model as model

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        c.status_message = []
        if not environ['PATH_INFO'].startswith("/error"):
            if 'portal_status_message' in session:
                c.status_message = session['portal_status_message']
                del session['portal_status_message']

        response = WSGIController.__call__(self, environ, start_response)

        session.save () # only save when there is no exception
        return response

# Include the '_' function in the public names
__all__ = [__name for __name in locals().keys() if not __name.startswith('_') \
           or __name == '_']
