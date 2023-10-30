# Author: Charles Jiron
# Date: 09-26-2023

# This script will grab all devices from Addigy, enumerate them, and save their names and serial numbers to a file.

import os
import requests
from requests import Response

# Main Function
def main():
    print("Fetching devices from Addigy...")
    save_devices_to_file(devices)
    print("Exiting...")

# Save Device Names and Serial Numbers to File
def save_devices_to_file(devices):
    with open("all_devices.txt", "w") as f:
        for idx, device in enumerate(devices, start=1):  # Starting index from 1
            serial_number = device.get('Serial Number', 'N/A')
            dev_name = device.get('Device Name', 'N/A')
            f.write(f"Device {idx}: Name: {dev_name}, Serial Number: {serial_number}\n")

# This is the main script to **Edit**
if __name__ == "__main__":
    # API Keys
    clientID = "-"
    clientSecret = "-"

    # Get the API URL to establish a Request
    url: str = f"https://prod.addigy.com/api/devices?client_id={clientID}&client_secret={clientSecret}"

    # Headers needed for the Request
    headers = {'Cookie': 'sessionid=e30:1qG4PW:8_g6N8G8V-JTli0SOM6tZNwXbcA'}

    # Will perform the API Request
    response: Response = requests.get(url, headers=headers)

    # Convert response to JSON
    devices = response.json()

    # Call the main function
    main()
    exit(0)
