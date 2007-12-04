"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to both as 'h'.
"""
from webhelpers import *
from pylons import session

def add_status_message(msg):
    if session["portal_status_message"]:
        session["portal_status_message"].append(msg)
    else:
        session["portal_status_message"] = [msg]
    session.save()
