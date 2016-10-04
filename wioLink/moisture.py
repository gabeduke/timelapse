import requests
import json
import datetime
from pymongo import MongoClient

#Mongo setup##
client = MongoClient()
db = client.moisture

server = "https://us.wio.seeed.io/v1"
token = "?access_token=eb306fbdff26c105bf271f7a4c24f91a"
node = "/node/GroveMoistureA0/moisture"
moist = requests.get(server + node + token

##FORMAT JSON##
today = datetime.datetime.now().strftime("%Y-%m-%d %H")
reading = moist.json()

data = {'reading': [reading]}
data['reading'].insert(0, {'date': today})

##INSERT DATA TO MONGODB##
insert = db.readings.insert_one(data)
