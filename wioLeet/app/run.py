#!/usr/bin/env python

from functions import *
from mailer import main

# wioMoistureStamp = get_wio_sensor_data(NodeProperties.moisture, wio_pete_token)
# wioHumidityStamp = get_wio_sensor_data(NodeProperties.humidity, wio1_token)
# wioTemperatureStamp = get_wio_sensor_data(NodeProperties.fahrenheit_degree, wio1_token)

wioMoistureStamp = get_wio_sensor_data2(moistureName, wio_moistureNode, wio_pete_token)
wioHumidityStamp = get_wio_sensor_data2(humidityName, wio_humidityNode, wio1_token)
wioTemperatureStamp = get_wio_sensor_data2(fahrenheit_degreeName, wio_tempNode, wio1_token)

data_dict = {NodeMap.moisture.value: wioMoistureStamp,
             NodeMap.humidity.value: wioHumidityStamp,
             NodeMap.temp.value: wioTemperatureStamp}

post_data_to_thinkspeak(data_dict)

post_data_to_initialstate(moistureName, wioMoistureStamp)
post_data_to_initialstate(humidityName, wioHumidityStamp)
post_data_to_initialstate(fahrenheit_degreeName, wioTemperatureStamp)

if wioMoistureStamp <= 450:
    main()
