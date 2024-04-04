## weather_api.py
import requests
import logging

class WeatherAPIError(Exception):
    """Base class for WeatherAPI exceptions"""
    pass

class NetworkError(WeatherAPIError):
    """Raised when a network error occurs"""
    pass

class APIError(WeatherAPIError):
    """Raised when the API returns a non-200 status code"""
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"API returned non-200 status code: {status_code}")

class WeatherAPI:
    """
    A class to fetch weather data using the OpenWeatherMap API.
    """
    def __init__(self, api_key: str = "YOUR_API_KEY"):
        """
        Initializes the WeatherAPI with a default or provided API key.

        Args:
            api_key (str): The API key for accessing the OpenWeatherMap API.
        """
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key

    def get_weather(self, location: str) -> dict:
        """
        Fetches the weather data for a given location.

        Args:
            location (str): The location for which to fetch the weather data.

        Returns:
            dict: A dictionary containing the weather data.
        """
        params = {
            "q": location,
            "appid": self.api_key,
            "units": "metric"  # Default to metric units.
        }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise APIError(response.status_code)
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error occurred while accessing {self.base_url}: {str(e)}")
            raise NetworkError(str(e))
