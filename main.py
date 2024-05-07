from flask import Flask, request, jsonify 
import requests

app = Flask(__name__)

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    api_key = 'bb0dc0b6bfa0f972218075b05863c88c'


    # Make API request to OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Extract relevant information
    temperature = data['main']['temp']
    condition = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    return jsonify({'city': city, 'temperature': temperature, 'condition': condition, 'humidity': humidity, 'wind_speed': wind_speed})

app.run(debug=True, host="0.0.0.0", port=8081)
