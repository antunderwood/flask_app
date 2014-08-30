from flask import Flask, render_template
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (views1)
from app.views1.controllers import views1
from app.views2.controllers import views2

# Register blueprint(s)
app.register_blueprint(views1)
app.register_blueprint(views2)

@app.route('/')
def index():
    return render_template('index.html')