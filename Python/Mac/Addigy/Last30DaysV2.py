# Author: Daryll Gomas
# Date: 10-30-2023

# This script will grab all devices from Addigy and identify 
# devices that were installed in the last 30 days.

# Python Library's
import os
import requests
from datetime import datetime, timedelta

# Check newly installed devices
def check_newly_installed(devices):
    print("Fetching devices from Addigy...")

    today = datetime.today()
    thirty_days_ago = today - timedelta(days=30)

    count_new_devices = 0

    # Open a text file in append mode
    with open('new_devices.txt', 'a') as file:
        file.write(f"\nResults as of {today.strftime('%Y-%m-%d %H:%M:%S')}:\n")
        file.write("-----------------------------------------------------\n")

        for device in devices:
            # Extracting the 'Registration Date'
            registration_date_str = device.get('Registration Date')
            
            # Extracting the 'Device Name' and 'Serial Number'
            device_name = device.get('Device Name')
            serial_number = device.get('Serial Number')

            if registration_date_str:
                # Adjusted the datetime format to match the format of the 'Registration Date'
                registration_date = datetime.strptime(registration_date_str, '%Y-%m-%dT%H:%M:%SZ')
                if registration_date > thirty_days_ago:
                    count_new_devices += 1
                    # Write the device details to the text file
                    file.write(f"Device ID: {device.get('id', 'N/A')}, Registration Date: {registration_date_str}, Device Name: {device_name}, Serial Number: {serial_number}\n")

        file.write(f"\n{count_new_devices} device(s) registered in the last 30 days.\n")
        file.write("-----------------------------------------------------\n")

    print(f"{count_new_devices} device(s) registered in the last 30 days:")
    print("Exiting...")




# This is the main script to **Edit**
if __name__ == "__main__":
    # API Keys
    clientID = "-"
    clientSecret = "-"
    currentPath = os.getcwd()

    # Get the working directory
    print(f'Get current working directory : {currentPath}')

    # Get the API URL to establish a Request
    url: str = "https://prod.addigy.com/api/devices?client_id=" + clientID + "&client_secret=" + clientSecret

    # The payloads and Headers needed for the Request
    payload = {}
    headers = {
        'Cookie': 'sessionid=e30:1qG4PW:8_g6N8G8V-JTli0SOM6tZNwXbcA'
    }

    # Will perform the API Request
    response = requests.request("GET", url, headers=headers, data=payload)

    # Devices will output into a JSON to access each key and value needed from API Request
    devices = response.json()

    # Call the function to check for newly installed devices
    check_newly_installed(devices)
