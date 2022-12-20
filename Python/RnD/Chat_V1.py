import requests
from bs4 import BeautifulSoup
import time
import re

# Send a login request to the website with your username and password
login_url = "https://app.wallstreet.io/"
form_data = { "username": "iccanui@gmail.com", "password": "B00mer11" }
response = requests.post(login_url, data=form_data)

# Parse the HTML content of the chatroom page and extract the messages
soup = BeautifulSoup(html_content, "html.parser")
messages = soup.find_all("div", class_="message")

# Iterate through the messages and extract the user's name and the message content
results = []
for message in messages:
    user_name = message.find("span", class_="user-name").text
    message_content = message.find("p", class_="message-content").text
    if user_name == "specified_name":
        # Check if the message was posted within the last 12 hours
        message_time = message.find("span", class_="message-time").text
        message_time = re.sub(r"\D", "", message_time)  # Extract the timestamp from the message time string
        current_time = int(time.time())
        if current_time - int(message_time) < 12 * 60 * 60:
            results.append((user_name, message_content))

# Return the list of messages
print(results)
