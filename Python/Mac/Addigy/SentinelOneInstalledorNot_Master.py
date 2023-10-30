# Author: Charles Jiron
# Date: 09-26-2023

# This script will grab all devices and separate them two different arrays:
# 1. Devices that has SentinelOne Installed
# 2. Devices that do not have Sentinel Installed

# Once in two separate arrays, we will place them in two separate files.

# Python Library's
import os
import requests
from requests import Response


# Main Function to call the SENTINEL ONE Check
def main():
    print("WELCOME TO THE SENTINEL ONE CHECK!...\n")
    SentinelOneCHECK(devices, device_name_serial_app_installed, sentinelInst ,sentinelNot)
    print("Exiting...")


# SENTINEL ONE Check
def SentinelOneCHECK(d, device_info, sen_Inst, senNot_Inst):
    while True:
        try:
            # Will open the created files for writing
            f = open("devicesSentinelInstalled.txt", "x")
            f_2 = open("devicesSentinelNotInstalled.txt", "x")

            # Will loop into our JSON for specific data
            for device in d:
                #############################################################################
                # Will Grab two data points of my custom fact, serial number, and device name.
                # It will then get added to our Dictionary
                # In the device sections,
                # You need to input your custom fact name device['YOUR SENTINEL ONE CUSTOM FACT NAME']
                device_info['SentinelOne Installed'] = device['SentinelOneValue']
                device_info['Serial Number'] = device['Serial Number']
                device_info['Device Name'] = device['Device Name']
                #############################################################################

                # Will Grab the string output for our conditional statement
                # Will Grab Serial Number and Device Name for our created list
                condition = device_info.get('SentinelOne Installed')
                serial_number = device_info.get('Serial Number')
                dev_name = device_info.get('Device Name')
                #############################################################################

                # Will Check the condition if True, append the device name, serial number and condition value.
                # Will also append, device name and serial number to a different list
                if condition == "SentinelOne Installed":
                    sen_Inst.append(f'\nName: {dev_name}')
                    sen_Inst.append(f'\nSerial Number: {serial_number}')
                    sen_Inst.append(f'\nValue: {condition}\n')


                # Will Check the condition if False, append the device name, serial number and condition value.
                # Will also append, device name and serial number to a different list
                if condition == "SentinelOne Not Installed" or condition is None:
                    senNot_Inst.append(f'\nName: {dev_name}')
                    senNot_Inst.append(f'\nSerial Number:{serial_number}')
                    senNot_Inst.append(f'\nValue: {condition}\n')

            #############################################################################
            # Will Call the File Creation Function and pass these arguments in it.
            fileCreation(senNot_Inst, sen_Inst, f, f_2)
            break
        except FileExistsError:
            # print("The File still exist, the file would get deleted, and it will try again.")
            os.remove('devicesSentinelInstalled.txt')
            os.remove('devicesSentinelNotInstalled.txt')
            continue


# The File Creation Function
def fileCreation(sen_file_not_installed, sen_file_installed, fcreation, fcreation_2):
    # Will output the Devices that have SentinelOne and the ones that do not have it
    # Finally it will output All devices and Serial Numbers

    # These variables will make the output it a little bit more readable.
    sen_result_Installed = ''.join(sen_file_installed)
    sen_result_Not_Installed = ''.join(sen_file_not_installed)

    # Output of Result
    print("#######################################################")
    print(f'All Devices having SentinelOne Installed: {sen_result_Installed}')
    print("#######################################################")
    print(f'All Devices having SentinelOne not Installed: {sen_result_Not_Installed}')
    print("#######################################################")

    ################################################################
    # This will output both results in a txt file
    fcreation.write(f"All Devices having SentinelOne Installed:\n"
                    f"{sen_result_Installed}\n")


    fcreation_2.write(f"All Devices having SentinelOne not Installed:\n"
                    f"-> {sen_result_Not_Installed}")


    fcreation.close()
    fcreation_2.close()
    print("Txt File Done...")
    #########################################################

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
    response: Response = requests.request("GET", url, headers=headers, data=payload)

    # Devices will output into a JSON to access each key and value needed from API Request
    devices = response.json()

    # Will establish these variables HERE to Output
    device_name_serial_app_installed = dict()
    sentinelInst = list()
    sentinelNot = list()


    # Will call the main function
    main()
    exit(1)
