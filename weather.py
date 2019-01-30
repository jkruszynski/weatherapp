import requests
from datetime import datetime
from flask import request
import sqlite3


weather_dict = {}


def get_weather(lat, long):
    print('get_weather')
    print(lat, long)
    # weather.com
    weather_api = requests.get('https://api.weather.gov/points/'+str(lat)+','+str(long))
    weather_api_dict = weather_api.json()
    forecast_url = weather_api_dict['properties']['forecast']
    forecast_request = requests.get(forecast_url)
    forecast_dict = forecast_request.json()
    weather_list = []
    for forecast in forecast_dict['properties']['periods']:
        weather_list.append(forecast['name'] + ': ' + forecast['detailedForecast'])

    weather_dict['weather.com'] = weather_list
    # pprint(forecast_dict)

    # dark skies
    dark_skies_r = requests.get('https://api.darksky.net/forecast/ffa912ad1451869fa8e5b73869e4e31b/'+str(lat)+','+str(long))

    dark_skies = dark_skies_r.json()

    # pprint(dark_skies['daily'])
    weather_list = []
    for f in dark_skies['daily']['data']:
        d = datetime.utcfromtimestamp(f['time']).strftime('%A')
        weather_str = d + ' -- '
        weather_str += 'High: ' + str(f['apparentTemperatureHigh']) + ', Low: ' + str(f['apparentTemperatureLow']) + ', '
        weather_str += f['summary']
        if 'precipType' in f.keys():
            weather_str += ' with a ' + str(f['precipProbability']) + ' probability of ' + f['precipType']
        weather_list.append(weather_str)
    weather_dict['Dark Skies'] = weather_list

    return weather_dict


def get_ip():
    print('get_ip')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']

    req = requests.get('http://api.ipstack.com/'+str(ip)+'?access_key=c3bc8b0532a448ed5b30b561715d428c')
    r = req.json()
    if r['latitude'] is None:
        req = requests.get('http://api.ipstack.com/'+'192.104.183.109'+'?access_key=c3bc8b0532a448ed5b30b561715d428c')
        r = req.json()

    return r


def zip_to_coords(user):
    print('zip_to_coords')
    conn = sqlite3.connect('simple_db.sqlite')
    c = conn.cursor()
    c.execute("select lat, lng, major_city from simple_zipcode where zipcode = " + user)
    result = c.fetchall()[0]
    conn.close()
    coords = (result[0], result[1])
    city = result[2]
    return coords, city


