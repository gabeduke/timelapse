from windMailer.mailer import SendMessage
import forecastio

api_key = "be063e11c53854ceb6e27afed0057aec"
lat = "37.5000327"
lng = "-77.5628374"


def sendMessage(message):
    to = "gabeduke@gmail.com"
    sender = "gabeduke@gmail.com"
    subject = "ALERT: Wind gonna blow!"
    msgHtml = message
    msgPlain = message
    SendMessage(sender, to, subject, msgHtml, msgPlain)


forecast = forecastio.load_forecast(api_key, lat, lng)
byDay = forecast.daily()

print "-------------------------- DAILY --------------------------"
for dailyData in byDay.data:
    wind = dailyData.windSpeed
    time = dailyData.time
    message = "Wind is expected to be " + str(wind) + "mph on " + str(time.day)

    if wind > 6:
        sendMessage(message)
