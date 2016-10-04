import plotly.plotly as py
import plotly.graph_objs as go
from pymongo import MongoClient

#Mongo setup
cred = "gabeduke:garrity@"
host = "programming.local:"
port = "27017"
client = MongoClient("mongodb://" + cred + host + port)
db = client.moisture

x = db.readings.moisture
y = 1023

trace = go.Scatter(x,y)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-line')