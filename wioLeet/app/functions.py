#!usr/bin/env python
import smtplib
from properties import *
from ISStreamer.Streamer import Streamer
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


def get_wio_sensor_data(nodeName, nodeValue, token):
    l = []
    for x in range(0, 3):
        req = requests.get(wio_url + nodeValue + token)

        resp_dict = json.loads(req.content)  # loads the request into a dictonary for parsing
        sensor_data = resp_dict[nodeName]  # parses the value from the request dictionary

        l.append(sensor_data)

    print(l)
    return mean(l)


def get_temperature(token):
    get_wio_sensor_data(NodeProperties.fahrenheit_degree.name, NodeProperties.fahrenheit_degree.value, token)


def get_humidity(token):
    get_wio_sensor_data(NodeProperties.humidity.name, NodeProperties.humidity.value, token)


def get_moisture(token):
    get_wio_sensor_data(NodeProperties.moisture.name, NodeProperties.moisture.value, token)


def get_airQuality(token):
    get_wio_sensor_data("airQuality", wio_airQuality, token)


def post_data_to_thinkspeak(data):
    payload = {'api_key': thingspeak_apiKey}
    payload.update(data)
    req = requests.post(thingspeak_url, data=payload)
    print(req.text)


def post_data_to_initialstate(field_name, sensor_value):
    streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=IS_ACCESS_KEY)

    # send some data
    streamer.log(field_name, sensor_value)

    # flush and close the stream
    streamer.close()

