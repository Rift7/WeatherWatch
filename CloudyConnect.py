from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def weather():
    # Get the weather data from the OpenWeatherMap API
    api_key = "YOUR_API_KEY"
    city = "New York"
    units = "imperial"  # Use Fahrenheit
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
    r = requests.get(api_url)
    weather_data = r.json()

    # Extract the necessary data from the API response
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    icon_url = f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png"

    # Render the template with the weather data
    return render_template("weather.html", temperature=temperature, description=description, icon_url=icon_url)

if __name__ == "__main__":
    app.run()
