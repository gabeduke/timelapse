#!usr/bin/env python  

import requests
import json
import datetime
import logging

##Enable Logging##
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

def formatUrl(node):

    return requests.get

def formatJson(x):
    reading = x.json()
    dump = json.dumps(reading)
    return json.loads(dump)

##GET data##
wio_url = "https://us.wio.seeed.io"
wio1_token = "?access_token=eb306fbdff26c105bf271f7a4c24f91a"
wio2_token = "?access_token=e8240174cbe8bf574cf9ef119fc1bfa6"
wio_moistureNode = "/v1/node/GroveMoistureA0/moisture"
wio_humidityNode = "/v1/node/GroveTempHumD0/humidity"
wio_tempNode = "/v1/node/GroveTempHumD0/temperature_f"
wio_airQuality = "/v1/node/GroveAirqualityA0/quality"

moisture = requests.get(wio_url + wio_moistureNode + wio1_token)
humidity = requests.get(wio_url + wio_humidityNode + wio1_token)
temp = requests.get(wio_url + wio_tempNode + wio1_token)
airQuality = requests.get(wio_url + wio_airQuality + wio2_token)

##FORMAT JSON##
today = datetime.datetime.now().strftime("%Y-%m-%d %H")

value = formatJson(moisture)
moisture = value['moisture']

value = formatJson(humidity)
humidity = value['humidity']

value = formatJson(temp)
temp = value['fahrenheit_degree']

value = formatJson(airQuality)
airQuality = value['quality']

##POST to Thinkspeak##
thingspeak_url = "https://api.thingspeak.com/update.json"
thingspeak_apiKey = "Y35LZQ4BTRZBMN37"
payload = {'api_key': thingspeak_apiKey, 'field5': airQuality, 'field2': moisture, 'field3': humidity, 'field4': temp}

req = requests.post(thingspeak_url, data=payload)
print(req.text)
