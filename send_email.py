import smtplib
import ssl
import streamlit as st

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "dr.has82@gmail.com"
    password = st.secrets["gmail_pass"]
    print(password)
    receiver = "dr.has82@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


