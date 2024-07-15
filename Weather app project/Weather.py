import requests
import json
import pyttsx3

while True:
    city = input("Enter the name of city: ")

    url = f"https://api.weatherapi.com/v1/current.json?key=9082d0f4f9214785a28144708232703&q={city}"

    r = requests.get(url)

    wdic = json.loads(r.text)
    w = wdic["current"]["temp_c"]
    s = wdic["current"]["wind_kph"]
    h = wdic["current"]["humidity"]
    d = wdic["current"]["last_updated"]

    engine = pyttsx3.init()

    x = f'''The current weather in {city} by last update date {d} the Temperature is {w} degrees celcius, wind speed 
    in Kilometer per hour  is {s}, and humidity is {h}, Thank you! for using weather application. '''

    print(x)
    engine.say(x)
    engine.runAndWait()
    engine.stop()
