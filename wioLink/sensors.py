#!usr/bin/env python
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


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def get_wio_sensor_data(node, token):
    l = []
    for x in range(0, 3):
        req = requests.get(wio_url + node.value + token)

        resp_dict = json.loads(req._content)  # loads the request into a dictonary for parsing
        sensor_data = resp_dict[node.name]  # parses the value from the request dictionary

        l.append(sensor_data)

    print l
    return mean(l)



def post_data_to_thinkspeak(fieldName, json):
    payload = {'api_key': thingspeak_apiKey, fieldName.value: json}
    req = requests.post(thingspeak_url, data=payload)
    print(req.text)


wioStamp = get_wio_sensor_data(NodeProperties.moisture, wio_pete_token)
post_data_to_thinkspeak(NodeMap.moisture, wioStamp)