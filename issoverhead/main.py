import requests
from datetime import datetime
import smtplib
import time
password = "your app password"
my_email = "your email address"
MY_LAT = 34.5553 # Your latitude
MY_LONG = 69.2075 # Your longitude

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    time_now = datetime.now()
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])#+your UTC
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])#+your UTC
    if (time_now.hour > sunset) or (time_now.hour < sunrise):
        return True
    else:
        return False


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    latitude = iss_latitude - MY_LAT
    longitude = iss_longitude - MY_LONG
    if (latitude < 5 and (latitude > -5)) and (longitude < 5 and (longitude > -5)):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_dark() and is_close():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
            to_addrs="target's email address",
            msg="Subject:ISS Overhead\n\nlook up at the sky!")




