import os
import smtplib

PASSWORD = os.getenv("PASSWORD")


def send_email():
    print("Email send")
