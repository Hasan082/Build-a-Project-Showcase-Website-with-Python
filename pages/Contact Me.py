import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Write your message")
    
    message = f"""\
Subject: Email from the website by {user_email}

From: {user_email}
{raw_message}
    """

    button = st.form_submit_button("Send Message")
       
    if button:
        if user_email and raw_message:  # Check that both fields are filled
            send_email(message)
            st.info("We received your email! I will contact you as soon as possible.")
        else:
            st.error("Please provide both an email address and a message.")