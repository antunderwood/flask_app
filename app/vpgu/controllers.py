# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask.ext.httpauth import HTTPDigestAuth

# authentication stuff
auth = HTTPDigestAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

# Define the blueprint: 'vpgu', set its url prefix: app.url/vpgu
vpgu = Blueprint('vpgu', __name__, url_prefix='/vpgu', template_folder='templates')

# Set the route and accepted methods
@vpgu.route('/page1')
@auth.login_required
def page1():
	return render_template('vpgu/page1.html')