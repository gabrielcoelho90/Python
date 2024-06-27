import requests

RETRIEVE_DATA_SHEET = "https://api.sheety.co/595483543bc076d86f26413ab4beb4c1/flightsPromotions/prices"


class DataManager:

    def __init__(self):
        self.sheet_data_params = {}
        self.iata = None
        self.city = None

    def sheet_info(self):
        rtv_response = requests.get(url=RETRIEVE_DATA_SHEET)
        data = rtv_response.json()
        return data

    def write_data_in_sheet(self, iata, city):
        self.city = city
        self.iata = iata
        sheet_data = self.sheet_info()['prices']
        print(sheet_data)
        for sheet in sheet_data:
            name_of_city = sheet['city']
            if city == name_of_city:
                id = sheet['id']
                print(id)
                print(name_of_city)
                edit_data_params = {
                    "price": {
                        "iataCode": iata
                    }
                }
                requests.put(url=f"{RETRIEVE_DATA_SHEET}/{id}", json=edit_data_params)

