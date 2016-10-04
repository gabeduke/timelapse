import requests
from pymongo import MongoClient

#Mongo setup
cred = "gabeduke:garrity@"
host = "programming.local:"
port = "27017"
client = MongoClient("mongodb://" + cred + host + port)
db = client.moisture

server = "https://us.wio.seeed.io/v1"
token = "?access_token=eb306fbdff26c105bf271f7a4c24f91a"
node = "/node/GroveMoistureA0/moisture"
moist = requests.get(server + node + token)

reading = moist.json()
insert = db.readings.insert_one(reading)

print insert.inserted_id
