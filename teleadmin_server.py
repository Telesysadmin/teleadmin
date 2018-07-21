#!/usr/bin/python3
# run from shell:
# FLASK_APP=teleadmin_server.py FLASK_DEBUG=1 flask run --port=80 --host=teleadmin.fvds.ru
# FLASK_ENV=DEBUG FLASK_DEBUG=1 flask run --port=443 --host=teleadmin.fvds.ru --cert=./cert/fullchain1.pem --key=./cert/privkey1.pem
import json
from flask import Flask, send_from_directory, request, make_response, Response, jsonify
import ssl
from utils import InvalidUsage, config
from platforms.vk.server import VkServer
from platforms.vk.client import VkClient




app = Flask(__name__)

host = config['SERVER_NAME']
port = config['PORT']

__all__ = ["app"]


class Dialog():
  def response_server_to_user(self, user_message):
    mes = "Твоё сообщение '{}' получено".format(user_message)
    VkClient().send_message(config["API"]["vk"]["peer_id"], mes)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route("/")
def hello():
  return "Welcome to Teleadmin api on server"

@app.route("/.well-known/acme-challenge/<path:filename>")
def letsencrypt_static(filename):
  return send_from_directory(app.root_path + '/.well-known/acme-challenge/', filename)

@app.route('/vk', methods=['POST'])
def vk():
  try:
    vkserver = VkServer()
    re = vkserver.call_type_func()
    dialog = Dialog()
    dialog.response_server_to_user(vkserver.user_message_text)

    return re
  except Exception as e:
    raise
    # return jsonify(e.args[0])




# context = ssl.create_default_context()
# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.verify_mode = ssl.CERT_REQUIRED
# context.load_cert_chain(certfile=config["SSL"]["cert"], keyfile=config["SSL"]["privkey"])
# context.load_verify_locations(cafile=config["SSL"]["client_cert"])

if __name__ == '__main__':
  # working:
  # app.run(host=host, port=port, ssl_context=(config["SSL"]["fullchain"], config["SSL"]["privkey"]))

  # for prod with uwsgi:
  app.run(host='127.0.0.1')
