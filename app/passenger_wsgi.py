import sys
import os

INTERP = "/home/arabblbo/virtualenv/public_html/arabity/app/3.13/bin/python"

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))

from asgiref.wsgi import WsgiToAsgi
from main import app as fastapi_app

application = WsgiToAsgi(fastapi_app)