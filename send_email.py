from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
import os


load_dotenv()

""" ADD Email Password """
password = os.getenv('EMAIL_APP_PASSWORD') 

def send_emails(receiver, sender, body, smtp, port):
    message = MIMEText()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Automated Email'
    
    
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp, port)
        server.starttls() # Enable security
        text = message.as_string()
        server.login(sender, receiver, text)
        server.quit()
        print("Email sent succcessfully")
    except Exception as ex:
        print(f"Failed to send email: {ex}")    