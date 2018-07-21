import json
from flask import request
from utils import InvalidUsage, config
import subprocess
from subprocess import PIPE, Popen


class Server():
  api_types = None
  current_response = None
  response_text = None
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
      self.current_response = self.api_types[self.type]
      return self.current_response["func"]()
    else:
      raise InvalidUsage("Unknown request type")

  def do_message(self, message):
    command = self.parse_message(message)
    requests = config['REQUESTS']
    if command in requests:
      if "file" in requests[command]:
        response = self.exec_script(requests[command])
        self.respone_text = response
        return response
      else:
        if command == "help":
          self.respone_text = self.help_message()
    else:
      self.respone_text = "Unknown command"


  def help_message(self):
    description_list = []
    for name in config['REQUESTS']:
      re = config['REQUESTS'][name]["description"]
      description_list.append("{} — {}".format(name, config['REQUESTS'][name]["description"]))
    ret = "\n".join(description_list)

    return ret
    # return re



  def parse_message(self, message):
    words = message.split(" ")
    command = words[0]
    return command

  def exec_script(self, scriptdata):

    try:
      script_file = scriptdata["file"]
      p = Popen(['bash','./scripts/request/{}'.format(script_file)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
      output, err = p.communicate()
      rc = p.returncode
    except Exception as e:
      print(e)
      return "Fail exec shell command"
    else:
      return output






