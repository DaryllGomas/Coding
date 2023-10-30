# Author: Charles Jiron
# Date: 09-26-2023 -10-23-2023

# This script will grab all devices and separate them into two different arrays:
# 1. Devices that have SentinelOne Installed
# 2. Devices that do not have Sentinel Installed

# Once in two separate arrays, we will place them in two separate files.

# Python Library's
import os
import requests
from requests import Response

# Target directory  
OUTPUT_DIRECTORY = "C:\\Users\\Staff\\Desktop"  

# Main Function to call the SENTINEL ONE Check
def main():
    print("WELCOME TO THE SENTINEL ONE CHECK!...\n")
    SentinelOneCHECK(devices, device_name_serial_app_installed, sentinelInst ,sentinelNot)
    print("Exiting...")

# SENTINEL ONE Check
def SentinelOneCHECK(d, device_info, sen_Inst, senNot_Inst):
    file_installed_path = os.path.join(OUTPUT_DIRECTORY, "devicesSentinelInstalled.txt")
    file_not_installed_path = os.path.join(OUTPUT_DIRECTORY, "devicesSentinelNotInstalled.txt")

    while True:
        try:
            f = open(file_installed_path, "x")
            f_2 = open(file_not_installed_path, "x")

            for device in d:
                device_info['SentinelOne Installed'] = device['SentinelOneValue']
                device_info['Serial Number'] = device['Serial Number']
                device_info['Device Name'] = device['Device Name']

                condition = device_info.get('SentinelOne Installed')
                serial_number = device_info.get('Serial Number')
                dev_name = device_info.get('Device Name')

                if condition == "SentinelOne Installed":
                    sen_Inst.append(f'\nName: {dev_name}')
                    sen_Inst.append(f'\nSerial Number: {serial_number}')
                    sen_Inst.append(f'\nValue: {condition}\n')

                if condition == "SentinelOne Not Installed" or condition is None:
                    senNot_Inst.append(f'\nName: {dev_name}')
                    senNot_Inst.append(f'\nSerial Number:{serial_number}')
                    senNot_Inst.append(f'\nValue: {condition}\n')

            fileCreation(senNot_Inst, sen_Inst, f, f_2)
            break
        except FileExistsError:
            os.remove(file_installed_path)
            os.remove(file_not_installed_path)
            continue

# The File Creation Function
def fileCreation(sen_file_not_installed, sen_file_installed, fcreation, fcreation_2):
    sen_result_Installed = ''.join(sen_file_installed)
    sen_result_Not_Installed = ''.join(sen_file_not_installed)

    print("#######################################################")
    print(f'All Devices having SentinelOne Installed: {sen_result_Installed}')
    print("#######################################################")
    print(f'All Devices having SentinelOne not Installed: {sen_result_Not_Installed}')
    print("#######################################################")

    fcreation.write(f"All Devices having SentinelOne Installed:\n{sen_result_Installed}\n")
    fcreation_2.write(f"All Devices having SentinelOne not Installed:\n-> {sen_result_Not_Installed}")

    fcreation.close()
    fcreation_2.close()
    print("Txt File Done...")

if __name__ == "__main__":
    clientID = "-"
    clientSecret = "-"
    currentPath = os.getcwd()
    print(f'Get current working directory : {currentPath}')
    
    url: str = "https://prod.addigy.com/api/devices?client_id=" + clientID + "&client_secret=" + clientSecret
    payload = {}
    headers = {'Cookie': 'sessionid=e30:1qG4PW:8_g6N8G8V-JTli0SOM6tZNwXbcA'}

    response: Response = requests.request("GET", url, headers=headers, data=payload)
    devices = response.json()

    device_name_serial_app_installed = dict()
    sentinelInst = list()
    sentinelNot = list()

    main()
    exit(0)
