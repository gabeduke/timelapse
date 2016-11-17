from functions import *

wioStamp = get_wio_sensor_data(NodeProperties.moisture, wio_pete_token)
post_data_to_thinkspeak(NodeMap.moisture, wioStamp)
