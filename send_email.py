import smtplib, ssl
from dotenv import load_dotenv
import os
# Load .env
if os.getenv("GMAIL_PASSWORD") is None:
    load_dotenv()

def get_password():
    # Check if running on GitHub Actions
    if os.getenv("GITHUB_ACTIONS") == "true":
        return os.getenv("GMAIL_PASSWORD")
    else:
        # Return password from .env file
        return os.getenv("GMAIL_PASSWORD_LOCAL")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "dr.has82@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")
    print(password)
    receiver = "dr.has82@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
