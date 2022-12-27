# WeatherWatch

WeatherWatch is a simple Python web application that displays live weather maps using the OpenWeatherMap API.
## Features

* Shows the current temperature and weather conditions for a given location
* Displays a live weather map using Leaflet.js
* Uses the OpenWeatherMap API to retrieve real-time weather data

## Requirements

* Python 3.x
* Flask
* Requests

## Installation

 Clone the repository:

`git clone https://github.com/hedgestur/WeatherWatch.git`

Install the dependencies:

`pip install -r requirements.txt`

Set the API_KEY environment variable to your OpenWeatherMap API key:

`export API_KEY=YOUR_API_KEY`

Run the application:

`python WeatherWatch.py`

## Usage

Open the application in your web browser at [http://localhost:5000](http://localhost:5000). Enter the name of a city to see the current weather conditions and a live weather map for that location.
## Credits

[OpenWeatherMap](https://openweathermap.org) for providing the weather data
[Leaflet.js](https://leafletjs.com) for the live weather map

## License

WeatherWatch is licensed under the MIT License. See the LICENSE file for details.
