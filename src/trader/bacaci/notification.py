import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Any

class Notification:

    def __init__(self):

        smtp_outlook = "smtp-mail.outlook.com"
        smtp_gmail = "smtp.gmail.com"

        # Connect to the SMTP server
        self.server = smtplib.SMTP(
            smtp_outlook,
            587 # Port for secure connection (TLS)
            )

        # Establish a secure connection
        try:
            self.server.connect()
            self.server.starttls()
        except ConnectionRefusedError:
            print("Hedef makine etkin olarak reddettiğinden bağlantı kurulamadı")
            exit(1)

        # Email configuration
        self.sender_email = "bhaskan@bacaciyatirim.com"
        password = "Bacaci1234"
        
        # Log in to your email account
        self.server.login(self.sender_email, password)

        # Create the email message
        self.msg = MIMEMultipart()
        self.msg["From"] = self.sender_email
        self.msg["Subject"] = "NOTIFICATION FROM BACACI TRADING BOT"

    def __call__(self, receiver_email, message):
        # Reciever's email
        self.msg["To"] = receiver_email
        self.msg.attach(MIMEText(message, "plain"))

        # Send the email
        text = self.msg.as_string()
        self.server.sendmail(self.sender_email, receiver_email, text)

        # Close the connection
        self.server.quit()