activate_this = '/home/anthony/Documents/flask_app/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/anthony/Documents/flask_app')
from app import app as application