## location_detector.py

import requests
from typing import List

class LocationDetector:
    """
    A class to detect the user's location based on their IP address and provide nearby location options.
    """

    def __init__(self, api_url: str = "http://ip-api.com/json/", timeout: int = 5):
        """
        Initializes the LocationDetector with a default API URL and timeout.

        :param api_url: The URL of the API to fetch the location information.
        :param timeout: The timeout for the API request in seconds.
        """
        self.api_url = api_url
        self.timeout = timeout

    def get_nearby_locations(self) -> List[str]:
        """
        Detects the user's location based on their IP address and returns a list of nearby locations.

        This method checks for the expected 'city' key in the API response to ensure the correct data format.

        :return: A list of nearby locations, or ['Unknown Location'] if an error occurs or the response format is unexpected.
        """
        try:
            response = requests.get(self.api_url, timeout=self.timeout)
            response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX or 5XX
            data = response.json()

            if 'city' in data:
                city = data['city']
                return [city]
            else:
                print("Unexpected response format.")
                return ['Unknown Location']
        except requests.ConnectionError:
            print("Network error: Please check your internet connection.")
            return ['Unknown Location']
        except requests.RequestException as e:
            print(f"Error fetching location: {e}")
            return ['Unknown Location']
