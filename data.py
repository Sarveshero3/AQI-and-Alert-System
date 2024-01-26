import xml.etree.ElementTree as ET

# Initialize an empty dictionary to store the data
data = {}

# Parse the XML file
tree = ET.parse(r"C:\Users\Sarvesh Chandran\Desktop\Passion\Python Files\Programs\Projects\data_aqi_cpcb.xml")
root = tree.getroot()

# Loop through the XML elements and extract the required information
for country in root.findall('Country'):
    country_id = country.get('id')
    state_data = {}
    for state in country.findall('State'):
        state_id = state.get('id')
        city_data = {}
        for city in state.findall('City'):
            city_id = city.get('id')
            station_list = []
            for station in city.findall('Station'):
                station_id = station.get('id')
                station_list.append(station_id)
            city_data[city_id] = tuple(station_list)
        state_data[state_id] = city_data
    data[country_id] = state_data


def select_state(data):
    states = data['India'].keys()  # Assuming you want to select from India
    print("Available States:")
    for idx, state in enumerate(states, start=1):
        print(f"{idx}. {state}")
    state_idx = int(input("Select a state (enter the number): ")) - 1
    selected_state = list(states)[state_idx]
    return selected_state

def select_city(data, selected_state):
    cities = data['India'][selected_state].keys()
    print(f"Cities in {selected_state}:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")
    city_idx = int(input("Select a city (enter the number): ")) - 1
    selected_city = list(cities)[city_idx]
    return selected_city

def select_station(data, selected_state, selected_city):
    stations = data['India'][selected_state][selected_city]
    print(f"Stations in {selected_city}:")
    for idx, station in enumerate(stations, start=1):
        print(f"{idx}. {station}")
    station_idx = int(input("Select a station (enter the number): ")) - 1
    selected_station = stations[station_idx]
    return selected_station

selected_state = select_state(data)
selected_city = select_city(data, selected_state)
selected_station = select_station(data, selected_state, selected_city)

# Now you can use selected_state, selected_city, and selected_station to further query your data.
print(f"Selected State: {selected_state}")
print(f"Selected City: {selected_city}")
print(f"Selected Station: {selected_station}")
