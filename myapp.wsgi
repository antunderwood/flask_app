activate_this = '/home/anthony/Documents/myapp/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/anthony/Documents/myapp')
from app import app as application