import smtplib
import ssl
import streamlit as st
from dotenv import load_dotenv
import os

# Load .env if running locally
if os.getenv("GMAIL_PASSWORD") is None:
    load_dotenv()

def get_password():
    # Check if running locally and secret exists
    if st.secrets and "GMAIL_PASSWORD" in st.secrets:
        return st.secrets["GMAIL_PASSWORD"]
    else:
        # Return password from .env file
        return os.getenv("GMAIL_PASSWORD_LOCAL")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "dr.has82@gmail.com"
    password = get_password()
    print(password)
    receiver = "dr.has82@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
