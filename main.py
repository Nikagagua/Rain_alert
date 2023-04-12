import requests
from twilio.rest import Client

url = 'https://api.openweathermap.org/data/3.0/onecall'
api_key = "80f5fa2469d3ed174548abb962559d24"

account_sid = 'AC050bc9904ce03eb22a6ad34cc427f5f1'
auth_token = 'e5b0348dda737aaa959e2844ebd34c08'
phone_number = '+15075981601'
my_phone_number = "your phone number"

MY_LONG = 44.8337
MY_LAT = 41.6941
CITY = 'Tbilisi,GE'
EXCLUDE = 'current,minutely,daily'

params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': api_key,
    'exclude': EXCLUDE,
}

response = requests.get(url=url, params=params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False
for i in range(len(weather_slice)):
    condition_code = weather_slice[i]['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=phone_number,
        to=my_phone_number,
    )
    print(message.status)
