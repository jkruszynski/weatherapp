from flask import Flask
from flask import render_template
from weather import get_weather
from weather import get_ip



application = Flask(__name__)

@application.route('/')
def index():
    ip = get_ip()
    w = get_weather(ip['latitude'], ip['longitude'])
    return render_template('index.html', data=w, addr=ip['city'])

if __name__ == '__main__':
    application.run(debug=True)