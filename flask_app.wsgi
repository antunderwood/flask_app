from os.path import expanduser
home_dir = expanduser("~")
activate_this = "%s/Documents/Python/flask_app/env/bin/activate_this.py" % home_dir
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, "%s/Documents/Python/flask_app" %s home_dir)
from app import app as application
