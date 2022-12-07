import smtplib
import imaplib

# Replace the placeholders with your own Gmail login credentials
gmail_user = "-"
gmail_password = "-"

# Set the email address of the recipient
to = "recipient@example.com"

# Set the subject and body of the email
subject = "Word cloud"
body = "Here is the word cloud you requested."

# Create an SMTP server object
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# Login to the Gmail account
server.login(gmail_user, gmail_password)

# Create an IMAP server object
imap_server = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to the Gmail account
imap_server.login(gmail_user, gmail_password)

# Select the INBOX folder
imap_server.select("INBOX")

# Set the email headers
headers = [
    "From: " + gmail_user,
    "Subject: " + subject,
    "To: " + to,
    "MIME-Version: 1.0",
    "Content-Type: multipart/mixed; boundary=frontier"
]

# Set the email body
body = "\r\n".join(headers) + "\r\n\r\n" + body + "\r\n"

# Open the file you want to attach
with open("C:\\WordCloud\\wordcloud.png", "rb") as file:
    # Read the file data
    data = file.read()

    # Set the email attachment
    attachment = "\r\n".join([
        "--frontier",
        "Content-Type: text/plain",
        "Content-Transfer-Encoding: base64",
        "",
        data.encode("base64"),
        "--frontier--"
    ])

    # Set the final email message
    message = body + attachment

# Send the email
server.sendmail(gmail_user, to, message)

# Close the SMTP and IMAP server objects
server.close()
imap_server.close()
