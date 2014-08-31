from flask import Flask, render_template

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (customers)
from app.customers.controllers import customers
from app.vpgu.controllers import vpgu

# Register blueprint(s)
app.register_blueprint(customers)
app.register_blueprint(vpgu)

@app.route('/')
def index():
    return render_template('index.html')