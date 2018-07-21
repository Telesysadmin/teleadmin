import json
from flask import request
from utils import InvalidUsage

class Server():
  api_types = None
  def __init__(self):
    try:
      self.data = json.loads(request.data.decode("utf-8"))
      self.type = self.data["type"]
    except Exception:
      self.data = request.form
      self.type = self.data["type"]

  def validation(self):
    pass

  def call_type_func(self):
    self.validation()
    if self.type in self.api_types:
      return self.api_types[self.type]["func"]()
    else:
      raise InvalidUsage("Unknown request type")

  def parse_message(self, message):
    words = message.split(" ")
    command = words[0]

