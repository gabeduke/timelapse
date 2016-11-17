#!usr/bin/env python
from enum import Enum
from properties import *

import requests
import json
import logging


class Nodes(Enum):
    moisture = wio_moistureNode


# # Enable Logging # #
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def format_url(node, token):
    req = requests.get(wio_url + node.value + token)
    return json.loads(node.name, req)


def post_data_to_thinkspeak(fieldName, json):
    payload = {'api_key': thingspeak_apiKey, fieldName.name: json}
    req = requests.post(thingspeak_url, data=payload)
    print(req.text)

node = Nodes.moisture
wioStamp = format_url(node, wio_pete_token)
post_data_to_thinkspeak(node, wioStamp)
