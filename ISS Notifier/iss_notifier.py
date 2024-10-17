from haversine import haversine,Unit
import requests as r
import datetime as dt
import smtplib as smtp
import time

EMAIL = "Your Email"
PASSWORD = "Your Password"
MY_LAT = #Your Latitude
MY_LNG = #Your Longitude
TIME_ZONE = #Your Time Zone (eg."Asia/Dhaka")
MY_POSITION = (MY_LAT,MY_LNG)

def iss_overhead():
    iss_response = r.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()
    iss_lat=  float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])
    iss_position = (iss_lat,iss_lng)
    distance = haversine(MY_POSITION,iss_position,unit=Unit.KILOMETERS)
    if distance <= 2300:#2300 for 5 minutes [speed 7.66km/s]
        return True

def is_dark():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0, #to make the time in 24 hour format
        "date":"today",
        "tzid": TIME_ZONE
    }
    sun_response = r.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    sun_data=sun_response.json()
    sun_data = sun_data["results"]
    sunrise_hour = int(sun_data["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    if time_now>=sunset_hour or time_now<=sunrise_hour:
        return True
while True:
    if iss_overhead() and is_dark():
        with smtp.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject: ISS \n\n ISS is Coming Overhead in 5 minutes"
            )
    time.sleep(60)