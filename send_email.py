import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "dr.has82@gmail.com"
password = "oiwckoqcgghsjsuo"

context = ssl.create_default_context()

receiver = "drhasan201@gmail.com"
message = """\
Subject: Hi!

How are you?
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
