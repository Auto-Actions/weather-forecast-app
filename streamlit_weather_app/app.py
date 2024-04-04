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
        self.api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        self.weather_api = WeatherAPI(self.api_key)
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
