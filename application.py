from flask import Flask
from flask import render_template
from weather import get_weather
from weather import get_ip



application = Flask(__name__)

@application.route('/')
def index():
    w = get_weather()
    ip = get_ip()
    return render_template('index.html', data=w, addr=ip)

if __name__ == '__main__':
    application.run(debug=True)