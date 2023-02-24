import os
import base64
from email import message_from_bytes
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from notion_client import Client

# Set up authentication for Gmail API
creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.readonly'])
service = build('gmail', 'v1', credentials=creds)

# Set up authentication for Notion API
notion = Client(auth=os.environ["NOTION_API_KEY"])
database_id = os.environ["NOTION_DATABASE_ID"]

# Define the search query for Gmail API
query = "subject:ticket#/assigned"

# Retrieve a list of messages matching the search query
result = service.users().messages().list(userId='me', q=query).execute()

# Loop through each message and extract the relevant information
for message in result['messages']:
    message_data = service.users().messages().get(userId='me', id=message['id']).execute()
    message_content = base64.urlsafe_b64decode(message_data['payload']['parts'][0]['body']['data']).decode('utf-8')
    parsed_message = message_from_bytes(message_content.encode('utf-8'))
    subject = parsed_message['subject']
    sender = parsed_message['from']
    date = parsed_message['date']
    body = parsed_message.get_payload()

    # Create a new page in Notion with the information extracted from the email
    new_page = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": subject
                    }
                }
            ]
        },
        "Sender": {
            "rich_text": [
                {
                    "text": {
                        "content": sender
                    }
                }
            ]
        },
        "Date": {
            "date": {
                "start": date.split(" (")[0]
            }
        },
        "Body": {
            "rich_text": [
                {
                    "text": {
                        "content": body
                    }
                }
            ]
        }
    }
    notion.pages.create(parent={"database_id": database_id}, properties=new_page)
