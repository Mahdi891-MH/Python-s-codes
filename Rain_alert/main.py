import requests
from twilio.rest import Client
MY_LAT = 34.5553
MY_LON = 69.2075

MY_KEY = "your key"
account_sid = "your account sid"
auth_token = "your auth token"
client = Client(account_sid, auth_token)
parameter = {
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid": MY_KEY,
    "cnt": 4
}
is_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
data = response.json()["list"]


weather_conditions = [weather for forecast in data for weather in forecast["weather"]]
for weather in weather_conditions:
    if weather["id"] < 700:
        is_rain = True


if is_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+16204980485",
        to="+93 74 472 2905",
    )
    print(message.status)


