from eyvind.lib.base import *

from formencode import Schema, Invalid
from formencode.validators import *

from pylons.decorators import validate
from pylons.decorators.rest import dispatch_on

from paste.wsgiwrappers import WSGIResponse
import re

class UniqueUsername(String):
    messages = {
            'in_use': 'The login name you selected is already in use or is not valid.  Please choose another.',
            'too_leet': 'This username contains the invalid character(s) %(chars)s',
            }
    letter_regex = re.compile(r'[a-zA-Z0-9_]')

    def validate_python(self, value, state):
        try:
            user = User.byUsername(value)
            raise Invalid(self.message("in_use", state), value, state)
        except SQLObjectNotFound:
            pass
        non_letters = self.letter_regex.sub('', value)
        if non_letters:
            raise Invalid(self.message("too_leet", state, chars=non_letters),
                          value, state)

class UniqueEmail(Email):

    messages = {
        'in_use': 'That email address is already in use.  Please choose another.',
        }

    def validate_python(self, value, state):
        Email.validate_python(self, value, state)
        try:
            user = User.byEmail(value)
            raise Invalid(self.message('in_use', state), value, state)
        except SQLObjectNotFound:
            pass

class SignupForm(Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    username = UniqueUsername(min=2)
    password = String(min=5, messages=dict(tooShort='Passwords must be at least %(min)s characters long',
                                           empty='Please enter a password'))
    confirm_password = String()
    fullname = String(not_empty=False)
    email = UniqueEmail()
    chained_validators = [FieldsMatch('password', 'confirm_password')]

class LoginForm(Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    username = String()
    password = String()
    came_from = String(not_empty=False, if_missing="")
    no_expire_cookie = StringBoolean(if_missing=False)

#this will be replaced by something from TeamRoller later.
import httplib2
from urllib import urlencode
def confirm_password(username, password):
    h = httplib2.Http()
    url = "%s/people/%s/get-hash" % (config['openplans_instance'], username)
    
    data = dict(__ac_password = password)
    body = urlencode(data)
    resp, content = h.request(url, method="POST", body=body, redirections=0)
    if content.startswith("__ac"):
        return content
    else:
        return False

class UserController(BaseController):

    
#     @dispatch_on(POST='do_signup')
#     def join(self):
#         if c.username:
#             return h.redirect_to("/")
#         return render('user/show_signup.mako')

#     def confirm(self):
#         user = User.byConfirm_key(request.params['key'])
#         if user.confirmed:
#             c.status_message="You have tried to activate an account that is not pending confirmation. Please sign in normally."
#             return h.redirect_to("/")
#         c.user = user
#         c.username = user.username
#         user.confirmed = True        
#         response.set_cookie(*cookieauth.make_cookie(user.username))
#         return h.redirect_to(action="profile_edit", first_login=True)

#     def do_signup(self):
#         if not request.params.get('task|validate'):
#             return self.signup_real()

#         try:
#             self.form_result = SignupForm().to_python(request.params)
#             errors = {}
#             #return good response
#         except Invalid, e:
#             errors = e.unpack_errors(False, '.', '-')

#         actual_errors = dict(("oc-%s-error" % field, {'action': 'copy', 'html': '', 'effects': 'highlight'}) for field in request.params)
#         for field, message in errors.items():
#             if message == "Missing value":
#                 continue
#             actual_errors["oc-%s-error" % field] = {'action': 'copy', 'html': message, 'effects': 'highlight'}
#         return h.oc_json_response(actual_errors)

#     @validate(schema=SignupForm(), form='join')
#     def signup_real(self):
#         p = dict(self.form_result)
#         del p['confirm_password']
#         user = create_user(**p)
#         c.status_message = "Thanks for joining OpenPlans, %s! A confirmation email has been sent to you with instructions on activating your account." % user.username
#         return MainController().index()

#     @dispatch_on(POST='do_forgot')
#     def forgot(self):
#         return render('user/show_login.mako')

#     def do_forgot(self):
#         username = request.params['username']
#         #first, try it as a username:
#         try:
#             user = User.byUsername(username)
#             c.status_message = "Your username is %s. If you would like to reset your password, please check your email account for further instructions." % username
#         except SQLObjectNotFound:
#             user = User.selectBy(email=username)
#             try:
#                 user = user[0]
#                 c.status_message = "Your username is %s. If you would like to reset your password, please check your email account for further instructions." % user.username
#             except IndexError:
#                 c.status_message = "We can't find your account. This could be because you have not yet completed your email confirmation."
#                 user = None

#         if user and user.confirmed:
#             user.confirm_key = uuid4()
#             body = """
# You requested a password reminder for your OpenPlans account. If you did not request this information, please ignore this message.

# To change your password, please visit the following URL:
# http://localhost:5000/reset-password?key=%s
# """ % (user.confirm_key)
#             send_mail('greetings@openplans.org', user.email, 'OpenPlans - Password reminder', body)
#         return render('user/show_login.mako')

#     @dispatch_on(POST='do_reset_password')
#     def reset_password(self):
#         c.key = request.params['key']
#         return render('user/newpassword.mako')

#     def do_reset_password(self):
#         try:
#             user = User.byUsername(request.params['userid'])
#         except SQLObjectNotFound:
#             c.status_message = 'There is no member named "%s".' % request.params['userid']
#             return h.redirect_to("/reset-password", key=c.key)

#         key = request.params['key']
#         if not user.confirm_key == key:
#             c.status_message = 'Password reset attempt failed. Did you mistype your username or password?'
#             return h.redirect_to("/") #the key is wrong.  They don't get another chance

#         if not request.params["password"] == request.params["password2"]:
#             c.status_message = 'Passwords do not match'
#             return h.redirect_to("/reset-password", key=c.key)

#         c.user = user # log user in so we can change password
#         c.username = user.username        
#         user.password = request.params["password"]
#         c.status_message = 'Welcome! Your password has been reset, and you are now signed in.'
#        return h.redirect_to("/people/%s/account" % c.username)

    def logout(self):
        c.user = User.byUsername('anonymous')
        c.username = ""
        response.set_cookie(*cookieauth.logout())
        c.status_message = "You have signed out."
        return MainController().index()


    @dispatch_on(POST='do_login')
    def login(self):
        c.came_from = request.params.get('came_from', '')
        return self.show_login()

    def show_login(self):
        if request.environ.get('REMOTE_USER'):
            #user is already logged in
            request.environ['SCRIPT_NAME'] = ""
            redirect_to("/")

        return render('user/show_login.mako')

    @validate(schema=LoginForm(), form='show_login')
    def do_login(self):
        username = self.form_result['username']
#         try:
#             user = User.byUsername(username)
#         except SQLObjectNotFound:
#             user = None
            

#         if not user or not user.check_password(request.params['password']) or not user.confirmed:

        cookie = confirm_password(username, self.form_result['password'])
        if not cookie:
            h.add_status_message('Please check your username and password. '
                                 'If you still have trouble, you can <a href'
                                 '="forgot">retrieve your sign in information'
                                 '</a>.')
            c.came_from = request.params.get('came_from', '')
            return render('user/show_login.mako')

#         session = environ['beaker.session']
#         now = time.time()

#         if not self.form_result['no_expire_cookie']:
#             session['expiration'] = now + (60 * 60 * 8)
            
#         session['username'] = username

#         session.save()

        response = WSGIResponse(code=303)

        came_from = self.form_result.get('came_from')
        if came_from:
            came_from += "?portal_status_message=Welcome!+You+have+signed+in."
            response.headers['Location'] = str(came_from)
        else:
            #FIXME: do we need to do something special to send
            #the user to the tour page on their first login?
            script_name = request.environ['SCRIPT_NAME']
            request.environ['SCRIPT_NAME'] = ''
            response.headers['Location'] = h.url_for(str("/people/%s/account?portal_status_message=Welcome!+You+have+signed+in." % username))
            request.environ['SCRIPT_NAME'] = script_name

        value = cookie.split("=")[1][1:-1] #strip quotes
        response.set_cookie("__ac", value)
        return response
