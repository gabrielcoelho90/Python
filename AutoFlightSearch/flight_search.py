import requests

FLIGHT_SEARCH_KEY = "YBk3c2xvHJ1KrKn9oRWgU5isLk4B4NQ7"
FS_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:
    def __init__(self):
        self.city = None

    def flight_search_info(self, city):
        self.city = city

        headers = {
            "apikey": FLIGHT_SEARCH_KEY
        }

        info_flight_params = {
            "term": self.city,
            "location_types": 'city'
        }
        flight_data = requests.get(url=f"{FS_ENDPOINT}/locations/query", params=info_flight_params, headers=headers)
        return flight_data

    def find_flight(self, iata):
        self.iata = iata
        headers = {
            "apikey": FLIGHT_SEARCH_KEY
        }

        find_flight_params = {
            "fly_from": 'GIG',
            "fly_to": iata,
            "date_from": '30/12/2023',
            "date_to": '30/06/2024',
            "one_for_city": 1,
            "adults": 1,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": 'GBP',
            "max_stopovers": 0
        }
        find_flight_response = requests.get(url=f"{FS_ENDPOINT}/v2/search", params=find_flight_params, headers=headers)
        find_flight_data = find_flight_response.json()
        print(find_flight_data)
        # city_to = find_flight_data['data'][0]['cityTo']
        price = find_flight_data['data'][0]['price']
        print(price)
        return price


fly_to_us = FlightSearch()
fly_to_us.find_flight("MIA")
