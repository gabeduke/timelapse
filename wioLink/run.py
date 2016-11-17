from wioLink.properties import *
from wioLink.functions import get_wio_sensor_data, post_data_to_thinkspeak

wioStamp = get_wio_sensor_data(NodeProperties.moisture, wio_pete_token)
post_data_to_thinkspeak(NodeMap.moisture, wioStamp)