from email.mime.text import MIMEText
import smtplib

# Replace the placeholders with your own email address and password
email = "YOUR_EMAIL_ADDRESS"
password = "YOUR_EMAIL_PASSWORD"

# Create a new email message
msg = MIMEText("Hello, this is a test email!")
msg["Subject"] = "Test Email"
msg["From"] = email
msg["To"] = email
# Use the smtplib library to send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)
import os
from glob import glob
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.encoders import encode_base64

# Replace "FOLDER_PATH" with the path to the folder you want to email
folder_path = "FOLDER_PATH"

# Create a new email message
msg = MIMEMultipart()
msg["Subject"] = "Folder Contents"
msg["From"] = email
msg["To"] = email

# Use the os and glob modules to list the files in the folder
for file_path in glob(os.path.join(folder_path, "*")):
    # Open the file in binary mode
    with open(file_path, "rb") as f:
        # Create a new MIMEBase object to represent the file
        part = MIMEApplication(f.read(), Name=file_path)

    # Encode the file in base64
    part = encode_base64(part)

    # Add the file to the email
    msg.attach(part)

# Use the smtplib library to send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)
