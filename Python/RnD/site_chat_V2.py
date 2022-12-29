import requests
from bs4 import BeautifulSoup

# Set the URL of the login page
login_url = "https://wallstreet.io/login"

# Set the login credentials
login_data = {
    "username": "iccanui@gmail.com",
    "password": "B00mer11"
}

# Send the POST request to the login page
response = requests.post(login_url, data=login_data)

# Check the status code to make sure the login was successful
if response.status_code == 200:
    # Login was successful
    print("Login successful")
else:
    # Login failed
    print("Login failed")

# Set the URL of the webchat page
chat_url = "https://app.wallstreet.io/chat/general-chat"

# Send a GET request to the webchat page
response = requests.get(chat_url)

# Parse the HTML of the webchat page
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with the class "mat-body-2" and the attribute "wstooltipposition" set to "right"
messages = soup.find_all("strong", class_="mat-body-2", wstooltipposition="right")

# Open a file to save the chat messages
with open("C:\\Users\\Iccanui\\Documents\\Git\\Coding\\Python\\RnD\\chat_messages.txt", "w") as f:
    # Iterate through the chat messages and write them to the file
    for message in messages:
        # Check the text of the element to see if it matches the username "fetersynergy"
        if message.text == "fetersynergy":
            # This is a message made by the user "fetersynergy", so write it to the file
            f.write(message.text + "\n")

print("Done!")
