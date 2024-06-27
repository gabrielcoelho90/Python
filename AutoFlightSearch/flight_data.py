import requests
from datetime import datetime, timezone

FLIGHT_SEARCH_KEY = "YBk3c2xvHJ1KrKn9oRWgU5isLk4B4NQ7"
FS_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightData:

    def flight_structure(self, iata):
        self.iata = iata
        headers = {
            "apikey": FLIGHT_SEARCH_KEY
        }

        find_flight_params = {
            "fly_from": 'LON',
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
        city_to = find_flight_data['data'][0]['cityTo']
        price = find_flight_data['data'][0]['price']
        fly_from_iata = find_flight_data['data'][0]['flyFrom']
        fly_to_iata = find_flight_data['data'][0]['flyTo']
        local_dep = find_flight_data['data'][0]['local_departure']
        d = datetime.fromisoformat(local_dep[:-1]).astimezone(timezone.utc)
        date_of_dep = d.strftime('%Y-%m-%d')
        local_arr = find_flight_data['data'][0]['local_arrival']
        dt = datetime.fromisoformat(local_dep[:-1]).astimezone(timezone.utc)
        date_of_arrival = dt.strftime('%Y-%m-%d')
        message = (f"Only £{price} to fly from London-{fly_from_iata} to {city_to}-{fly_to_iata}\n"
                   f"from {date_of_dep} to {date_of_dep}")
        return message

