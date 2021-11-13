import smtplib
from email.message import EmailMessage


def send_email(content):
    msg = EmailMessage()
    msg.set_content(content)
    recipients = ['x@x.com']
    msg['From'] = 'y@y.com'
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'Changes to Parliament Order Paper'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('y@y.com', 'password')
    server.send_message(msg)
    server.quit()
