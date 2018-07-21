from utils import config
import time
from subprocess import Popen, PIPE
from platforms.vk.client import VkClient

class Monitoring():
  problems = {}

  def start(self):
    self.onetime()

  def onetime(self):
    try:
      for script in config["MONITORING"]["scripts"]:
        p = Popen(['bash','./scripts/monitoring/{}.sh'.format(script)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        rc = p.returncode
        message = output
        if rc != 0:
          self.problem(script, message)
        else:
          self.problem_resolved(script)

    except Exception as e:
      return "Fail exec shell command"
    time.sleep(config["MONITORING"]["INTERVAL"])
    self.onetime()

  def problem(self, script, message):
    if script in self.problems:
      if time.time() - self.problems[script] >= config["MONITORING"]["problem_lifetime"]:
        VkClient().send_message(config["API"]["vk"]["peer_id"], message)
    else:
      self.problems[script] = time.time()
      VkClient().send_message(config["API"]["vk"]["peer_id"], message)

  def problem_resolved(self, script):
    if script in self.problems:
      VkClient().send_message(config["API"]["vk"]["peer_id"], "Проблема {} решена".format(script))
      del self.problems[script]