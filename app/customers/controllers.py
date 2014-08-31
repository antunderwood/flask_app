# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for


# Define the blueprint: 'customers', set its url prefix: app.url/customers
customers = Blueprint('customers', __name__, url_prefix='/customers', template_folder='templates')

# Set the route and accepted methods
@customers.route('/page1')
def page1():
	return render_template('customers/page1.html')