#!usr/bin/env python
from enum import Enum
from properties import *

import requests
import json
import logging


# # Enable Logging # #
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def format_url(node, token):
    req = requests.get(wio_url + node.value + token)
    print req.text

    resp_dict = json.loads(req._content)  # loads the request into a dictonary for parsing
    return resp_dict[node.name]  # parses the value from the request dictionary


def post_data_to_thinkspeak(fieldName, json):
    payload = {'api_key': thingspeak_apiKey, fieldName.value: json}
    req = requests.post(thingspeak_url, data=payload)
    print(req.text)


wioStamp = format_url(NodeProperties.moisture, wio_pete_token)
post_data_to_thinkspeak(NodeMap.moisture, wioStamp)
