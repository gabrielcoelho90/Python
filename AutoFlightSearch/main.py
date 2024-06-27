#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from twilio.rest import Client

account_sid = 'xxxxx'
auth_token = 'xxxxxx'

sheet_data = DataManager()
json_sheet_data = sheet_data.sheet_info()
print(json_sheet_data)
sheet_price_list = [54, 42, 485, 551, 95, 414, 240, 260, 378]

# get_flight_info = FlightSearch()

get_iata = FlightSearch()
city = "Cape Town"
all_flight_data = get_iata.flight_search_info(city).json()
iata = all_flight_data['locations'][0]['code']


# write_iata_in_sheet = DataManager()
# write_iata_in_sheet.write_data_in_sheet(iata, city)

flight_search = FlightSearch()
flight_data = FlightData()
fly_to_list = ['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']
flight_prices = []
for fly in fly_to_list:
    new_price = flight_search.find_flight(fly)
    flight_prices.append(new_price)
    pos = fly_to_list.index(fly)
    # if flight_prices[pos] < sheet_price_list[pos]:
        # sms = flight_data.flight_structure(fly)
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     body=f"Low Price ALERT!\n{sms}",
        #     from_='+15204474330',
        #     to='+5521979798100')
        # print(message.sid)



