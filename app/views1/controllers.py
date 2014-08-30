# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for


# Define the blueprint: 'views1', set its url prefix: app.url/views1
views1 = Blueprint('views1', __name__, url_prefix='/views1', template_folder='templates')

# Set the route and accepted methods
@views1.route('/page1')
def page1():
	return render_template('page1.html')