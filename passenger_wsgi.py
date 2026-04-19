# INTERP = "/home/arabblbo/virtualenv/public_html/arabity/app/3.13/bin/python"

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app.main import app
from a2wsgi import ASGIMiddleware

application = ASGIMiddleware(app)