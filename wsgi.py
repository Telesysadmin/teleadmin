#!/usr/bin/python3
from gevent.pywsgi import WSGIServer
from teleadmin_server import app as application
from utils import config
import subprocess

if __name__ == "__main__":
    # application.run()
    http_server = WSGIServer(('0.0.0.0', 443), application,
                           keyfile=config["SSL"]["privkey"], certfile=config["SSL"]["fullchain"])
    http_server.serve_forever()
