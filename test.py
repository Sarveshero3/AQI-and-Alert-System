import data
from data import selected_station

import requests
import csv
from io import StringIO
import time

# Define your list of API keys
api_keys = [
    'API KEYS HERE, copy ->> https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69'
]

# Define the number of offset partitions
num_partitions = len(api_keys)

# Define the total number of data points
total_data_count = 3121

# Calculate the offsets for each API key
offsets = []
offset_step = total_data_count // num_partitions
for i in range(num_partitions):
    start_offset = i * offset_step
    end_offset = start_offset + offset_step - 1
    if i == num_partitions - 1:
        end_offset = total_data_count - 1
    offsets.append((start_offset, end_offset))

def get_air_quality_for_station(target_station, max_attempts=20, time_threshold=10):
    for i, api_key in enumerate(api_keys):
        start_offset, end_offset = offsets[i]
        print(f"Using API key: {api_key}")
        print(f"Offset Range: {start_offset} to {end_offset}")
        for _ in range(max_attempts):
            # Record the start time
            start_time = time.time()

            # Construct the API URL with the current API key and offset range
            api_url = f'https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key={api_key}&format=csv&offset={start_offset}&limit={end_offset - start_offset + 1}'

            # Make an HTTP GET request to the API
            response = requests.get(api_url)

            if response.status_code == 200:
                # Calculate the time taken
                end_time = time.time()
                time_taken = end_time - start_time

                # Check if the time taken exceeds the threshold
                if time_taken > time_threshold:
                    print(f"Please wait, it's taking longer than {time_threshold} seconds...")

                # Assuming the API response is in CSV format, parse it
                csv_data = response.text

                # Create a CSV reader from the response text
                csv_reader = csv.DictReader(StringIO(csv_data))

                # Loop through the CSV data to find the specific row
                for row in csv_reader:
                    if row['station'] == target_station:
                        print("Air Quality Data for the Selected Station:")
                        print(f"State: {row['state']}")
                        print(f"City: {row['city']}")
                        print(f"Station: {row['station']}")
                        print(f"Last Update: {row['last_update']}")
                        print(f"Pollutant ID: {row.get('pollutant_id', 'N/A')}")
                        print(f"Pollutant Min: {row.get('pollutant_min', 'N/A')}")
                        print(f"Pollutant Max: {row.get('pollutant_max', 'N/A')}")
                        print(f"Pollutant Avg: {row.get('pollutant_avg', 'N/A')}")
                        return  # Stop after finding the target row

            else:
                print(f"Failed to retrieve air quality data. Status code: {response.status_code}")

    print(f"Station '{target_station}' not found in the data after {max_attempts * len(api_keys)} attempts.")

# Replace 'Your Target Station Name' with the station name you want to select
get_air_quality_for_station(selected_station, time_threshold=10)
