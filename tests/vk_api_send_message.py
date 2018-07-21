#!/usr/bin/python3
import sys
sys.path.append("../")
from platforms.vk.client import VkClient

VkClient().send_message(575780, "Ко мне постучался косматый геолог")
