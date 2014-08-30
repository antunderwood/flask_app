# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for


# Define the blueprint: 'views2', set its url prefix: app.url/views2
views2 = Blueprint('views2', __name__, url_prefix='/views2', template_folder='templates')

# Set the route and accepted methods
@views2.route('/page1')
def page1():
	return render_template('views2/page1.html')