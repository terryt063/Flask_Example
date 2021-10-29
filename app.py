from flask import Flask
import random

app = Flask(__name__)

def getTemp(location):
    # get a random temperature for the location
    temp = {'location': location, 'temperature': (random.randint(5,25)), 'unit': 'Celcius'}
    return temp

def getWind(location):
    windDir = random.randint(0,360)
    windSpeed = random.randint(0,20)
    wind = {'location': location, 'wind_speed': windSpeed, 'wind_direction': windDir}
    return wind

@app.route("/temp/<location>")
def temp(location):
    if location == '':
        return 'No location entered'
    else:
        return getTemp(location)

@app.route("/wind/<location>")
def wind(location):
    if location == '':
        return 'No location entered'
    else:
        return getWind(location)
