from flask import Flask
import json
import codecs

app = Flask(__name__)
app.config.from_json("config.json")
config = app.config

class InvalidUsage(Exception):
  status_code = 400

  def __init__(self, message, status_code=None, payload=None):
    Exception.__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code
    self.payload = payload

  def to_dict(self):
    rv = dict(self.payload or ())
    rv['message'] = self.message
    self.args = list(self.message)
    return rv
#
# with open("./config.json", 'r') as fh:
#   config = json.loads(fh.read())
#   print(config)
# r = codecs.open("config.json", encoding='UTF-8')
# print(r.read())
