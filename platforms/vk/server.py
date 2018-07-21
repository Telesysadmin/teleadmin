import json
from flask import request
from utils import InvalidUsage, config
from server.Server import Server


class VkServer(Server):
  def __init__(self):
    super().__init__()
    self.api_types = {
      "confirmation": {
        "func": self.confirmation
      },
      "message_new": {
        "func": self.message_new,
        "send_response": True
      }
    }

  def validation(self):
    super().validation()
    try:
      if str(self.data["secret_key"]) != str(config["API"]["vk"]["secret_key"]):
        raise InvalidUsage("Bad vk secret_key", status_code=503)
    except Exception as e:
      if hasattr(e, 'message'):
        raise
      else:
        InvalidUsage("Fail validation: {}".format(e.args[0]))

  def confirmation(self):
    try:
      if str(self.data["group_id"]) == str(config["API"]["vk"]["group_id"]):
        return str(config["API"]["vk"]["confirm"])
      else:
        raise InvalidUsage('Confirmation is fail', status_code=503)
    except Exception as e:
      raise InvalidUsage('Confirmation error', status_code=410)

  def message_new(self):
    # data example: {"type": "group_join", "object": {"text": "xzc", "from_id": 1, "peer_id": 1, "attachments": [], "id": 27, "out": 1, "is_hidden": false, "conversation_message_id": 27, "important": false, "fwd_messages": [], "random_id": 0, "date": 1532054458}, "group_id": 1}
    try:
      self.user_message_object = self.data["object"]
      self.user_message_text = self.user_message_object["text"]
    except Exception as e:
      raise InvalidUsage("Failed parse data message_new")
    else:
      response = self.do_message(self.user_message_text)
      return "ok"
