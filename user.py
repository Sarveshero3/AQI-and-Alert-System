
import data

def select_state(data):
    states = data.keys()
    print("Available States:")
    for idx, state in enumerate(states, start=1):
        print(f"{idx}. {state}")
    state_idx = int(input("Select a state (enter the number): ")) - 1
    selected_state = list(states)[state_idx]
    return selected_state

def select_city(data, selected_state):
    cities = data[selected_state].keys()
    print(f"Cities in {selected_state}:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")
    city_idx = int(input("Select a city (enter the number): ")) - 1
    selected_city = list(cities)[city_idx]
    return selected_city

def select_station(data, selected_state, selected_city):
    stations = data[selected_state][selected_city]
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
