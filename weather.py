import requests
from pprint import pprint

weather_dict = {}

def get_weather():


    # weather.com
    weather_api = requests.get('https://api.weather.gov/points/'+'38.6247,-90.1848')
    weather_api_dict = weather_api.json()
    forecast_url = weather_api_dict['properties']['forecast']
    forecast_request = requests.get(forecast_url)
    forecast_dict = forecast_request.json()
    weather_list = []
    for forecast in forecast_dict['properties']['periods']:
        #weather_list.append(forecast['name'] + ': ' + forecast['shortForecast'] + ', ' + str(forecast['temperature']) +
         #                   forecast['temperatureUnit'] + '\n')
        weather_list.append(forecast['name'] + ': ' + forecast['detailedForecast'])

    weather_dict['weather.com'] = weather_list
    #pprint(forecast_dict)

    #openweather
    open_api = requests.get('http://api.openweathermap.org/data/2.5/forecast?zip=63104,us&APPID=656a6a0c523b77b982cd4867f6617c15&units=imperial')

    pprint(open_api.json())

    return weather_dict

get_weather()
