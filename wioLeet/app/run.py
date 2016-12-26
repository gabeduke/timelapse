from functions import *

wioMoistureStamp = get_moisture(wio_pete_token)
wioHumidityStamp = get_humidity(wio_pete_token)
wioTempStamp = get_temperature(wio_pete_token)

#post data to thingspeak
data_dict = {NodeMap.humidity.value: wioHumidityStamp,
             NodeMap.temp.value: wioTempStamp,
             NodeMap.moisture.value: wioMoistureStamp}

post_data_to_thinkspeak(data_dict)

#post data to initial state
post_data_to_initialstate(NodeMap.moisture.name, wioMoistureStamp)
post_data_to_initialstate(NodeMap.humidity.name, wioHumidityStamp)
post_data_to_initialstate(NodeMap.temp.name, wioTempStamp)
