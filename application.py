from flask import Flask
from flask import render_template, redirect
from weather import get_weather
from weather import get_ip
from weather import zip_to_coords
from form import ZipcodeForm

application = Flask(__name__)
application.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@application.route('/', methods=['GET', 'POST'])
def index():
    form = ZipcodeForm()
    print(form.zipcode.data)
    if form.zipcode.data is None:
        ip = get_ip()
        coords = ip['latitude'], ip['longitude']
        city = ip['city']
    else:
        coords, city = zip_to_coords(form.zipcode.data)

    w = get_weather(coords[0], coords[1])
    return render_template('index.html', data=w, addr=city, form=form)


if __name__ == '__main__':
    application.run(debug=True)