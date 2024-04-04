import streamlit as st
import requests
import os

from weather_api import WeatherAPI
from location_detector import LocationDetector

class StreamlitUI:
    def display_location_options(self, locations: list):
        """
        Display location options for the user to select from.
        """
        return st.selectbox("Select your location", locations)

    def display_weather_info(self, weather_info: dict):
        """
        Display the weather information.
        """
        if not weather_info:
            st.write("No weather information available.")
            return
        st.write("Weather Information:")
        for key, value in weather_info.items():
            st.write(f"{key}: {value}")

class App:
    def __init__(self):
        self.ui = StreamlitUI()
        self.weather_api = WeatherAPI()
        self.location_detector = LocationDetector()

    def run(self):
        """
        Main method to run the app.
        """
        locations = self.location_detector.get_nearby_locations()
        if not locations:
            st.write("Unable to detect locations. Please try again later.")
            return
        selected_location = self.ui.display_location_options(locations)
        weather_info = self.weather_api.get_weather(selected_location)
        self.ui.display_weather_info(weather_info)

if __name__ == "__main__":
    app = App()
    app.run()

## weather_api.py
import requests
import os

class WeatherAPI:
    def get_weather(self, location: str):
        api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        if not api_key:
            print("API key for OpenWeatherMap is not set.")
            return {}
        try:
            response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")
            response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return {}
