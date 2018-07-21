import json
import requests
from flask import request
from utils import InvalidUsage, config

class VkClient():
  def api_call(self, method, **kwargs):
    params = {}
    for key, value in kwargs.items():
      params[key] = value

    params["access_token"] = config["API"]["vk"]["access_token"]
    params["v"] = config["API"]["vk"]["version"]

    response = requests.get("{}{}".format(config["API"]["vk"]["url"], method), params=params)
    return response.json()

  def send_message(self, peer_id, message, attachments = None):
    if attachments is None:
      attachments = []
    self.api_call("messages.send", peer_id=peer_id, message=message, attachments=",".join(attachments))

