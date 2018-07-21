#!/usr/bin/python3
#  -*- coding: utf-8 -*-
from gevent.pywsgi import WSGIServer
from teleadmin_server import app as application
from utils import config
from multiprocessing import Process
import threading
from subprocess import Popen, PIPE
from server.Monitoring import Monitoring
import time


def start_monitoring():
  Monitoring().start()

if __name__ == '__main__':
  print("monitoring started")
  p = Process(target=start_monitoring)
  p.start()

if __name__ == "__main__":
  # application.run()
  print("http server started")
  http_server = WSGIServer(('0.0.0.0', 443), application,
                           keyfile=config["SSL"]["privkey"], certfile=config["SSL"]["fullchain"])
  http_server.serve_forever()
