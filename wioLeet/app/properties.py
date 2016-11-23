from enum import Enum


# # GET data # #
wio_url = "https://us.wio.seeed.io"
wio1_token = "?access_token=6da94989e6da2106dc7f8d569cc52a3c"
wio_pete_token = "?access_token=5d56c05c82d1e2453f9dcaa0bb59144c"
wio_moistureNode = "/v1/node/GroveMoistureA0/moisture"
wio_humidityNode = "/v1/node/GroveTempHumD0/humidity"
wio_tempNode = "/v1/node/GroveTempHumD0/temperature_f"
wio_airQuality = "/v1/node/GroveAirqualityA0/quality"

thingspeak_url = "https://api.thingspeak.com/update.json"
thingspeak_apiKey = "Y35LZQ4BTRZBMN37"

# The name your bucket will appear with in Initial State
BUCKET_NAME = "Dashboard"
# The hidden bucket key that associates the data w/a particular bucket
BUCKET_KEY = "D9DPURKHQSED"
# Initial State access key - found under "Account"
IS_ACCESS_KEY = "5al79nGUd8wzfasZIeVE4IHAB3PRbaqJ"


moistureName = "moisture"
humidityName = "humidity"
fahrenheit_degreeName = "fahrenheit_degree"
airQualityName = "airQuality"


class NodeProperties(Enum):
    moisture = wio_moistureNode
    humidity = wio_humidityNode
    fahrenheit_degree = wio_tempNode
    airQuality = wio_airQuality


# this fuction maps the fields in the Thingspeak dashboard
class NodeMap(Enum):
    moisture = 'field1'
    humidity = 'field2'
    temp = 'field3'
    airQuality = 'field4'
