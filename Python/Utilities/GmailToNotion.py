import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from notion_client import Client
from email.parser import BytesParser
from email.policy import default
from bs4 import BeautifulSoup

# Set up Notion client
os.environ["NOTION_API_KEY"] = "Enter You Notion API Key"
notion = Client(auth=os.environ["NOTION_API_KEY"])
database_id = "Enter the Database ID"  # Replace with your Notion database ID

# Set up Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('C:/Users/(Enter your account name on windows machine)/Documents/scripts/credentials.json', SCOPES)

        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

gmail_service = build('gmail', 'v1', credentials=creds)

from bs4 import BeautifulSoup

def create_notion_page(subject, body):
    soup = BeautifulSoup(body, 'html.parser')
    
    # Remove all links
    for a in soup.find_all('a'):
        a.replace_with(soup.new_string(a.string))
    
    # Get the text content without HTML tags
    text_content = soup.get_text()
    
    # Remove extra newlines
    lines = text_content.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    cleaned_text_content = '\n'.join(cleaned_lines)
    
    #Truncate to include only the first 2000 characters
    if len(cleaned_text_content) > 2000:
        cleaned_text_content = cleaned_text_content[:2000]
    
    new_page = {
        "Subject": {"title": [{"text": {"content": subject}}]},
        "Email Body": {"rich_text": [{"text": {"content": cleaned_text_content}}]},
    }
    notion.pages.create(parent={"database_id": database_id}, properties=new_page)



def process_emails():
    results = gmail_service.users().messages().list(userId='me', q="subject:assigned is:unread").execute()
    emails = results.get('messages', [])

    for email in emails:
        msg = gmail_service.users().messages().get(userId='me', id=email['id'], format='raw').execute()
        msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
        
        email_message = BytesParser(policy=default).parsebytes(msg_str)
        subject = email_message['subject']
        body = email_message.get_body(preferencelist=('plain',)).get_content()
        
        if subject and body:
            create_notion_page(subject, body)
            gmail_service.users().messages().modify(userId='me', id=email['id'], body={'removeLabelIds': ['UNREAD']}).execute()

if __name__ == '__main__':
    process_emails()