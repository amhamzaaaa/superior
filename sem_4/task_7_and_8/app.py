from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = '348882c45264cfc8d94059c624c6e826'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        params = {'q': city, 'appid': API_KEY}
        response = requests.get(WEATHER_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            temperature = round(data['main']['temp'] - 273.15, 1)
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            return render_template('index.html', 
                                 city=city, 
                                 temperature=temperature, 
                                 humidity=humidity, 
                                 description=description)
        else:
            if response.status_code == 404:
                error = 'City not found'
            elif response.status_code == 401:
                error = 'Invalid API key'
            else:
                error = f'API error: {response.status_code}'
            return render_template('index.html', error=error)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)