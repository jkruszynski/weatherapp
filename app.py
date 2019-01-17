from flask import Flask
from flask import render_template
from weather import get_weather



app = Flask(__name__)

@app.route('/')
def index():
    w = get_weather()
    return render_template('index.html', data=w)

if __name__ == '__main__':
    app.run(debug=True)