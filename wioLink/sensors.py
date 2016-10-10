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

##GET data##
wio_url = "https://us.wio.seeed.io/v1"
wio_token = "?access_token=eb306fbdff26c105bf271f7a4c24f91a"
wio_moistureNode = "/node/GroveMoistureA0/moisture"
wio_humidityNode = "/node/GroveTempHumD0/humidity"
wio_tempNode = "/node/GroveTempHumD0/temperature_f"

moisture = requests.get(wio_url + wio_moistureNode + wio_token)
humidity = requests.get(wio_url + wio_humidityNode + wio_token)
temp = requests.get(wio_url + wio_tempNode + wio_token)

##FORMAT JSON##
today = datetime.datetime.now().strftime("%Y-%m-%d %H")

def formatJson(x):
    reading = x.json()
    dump = json.dumps(reading)
    return json.loads(dump)

value = formatJson(moisture)
moisture = value['moisture']

value = formatJson(humidity)
humidity = value['humidity']

value = formatJson(temp)
temp = value['fahrenheit_degree']

##POST to Thinkspeak##
thingspeak_url = "https://api.thingspeak.com/update.json"
thingspeak_apiKey = "Y35LZQ4BTRZBMN37"
payload = {'api_key': thingspeak_apiKey, 'field2': moisture, 'field3': humidity, 'field4': temp}

req = requests.post(thingspeak_url, data=payload)
print(req.text)
