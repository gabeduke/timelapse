from wioLink import *


# # GET data # #
wio_url = "https://us.wio.seeed.io"
wio1_token = "?access_token=eb306fbdff26c105bf271f7a4c24f91a"
wio_pete_token = "?access_token=5d56c05c82d1e2453f9dcaa0bb59144c"
wio_moistureNode = "/v1/node/GroveMoistureA0/moisture"
wio_humidityNode = "/v1/node/GroveTempHumD0/humidity"
wio_tempNode = "/v1/node/GroveTempHumD0/temperature_f"
wio_airQuality = "/v1/node/GroveAirqualityA0/quality"

thingspeak_url = "https://api.thingspeak.com/update.json"
thingspeak_apiKey = "Y35LZQ4BTRZBMN37"


class NodeProperties(Enum):
    moisture = wio_moistureNode
    humidity = wio_humidityNode
    temp = wio_tempNode
    airQuality = wio_airQuality


class NodeMap(Enum):
    moisture = 'field1'
    humidity = 'field2'
    temp = 'field3'
    airQuality = 'field4'
