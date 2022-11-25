import firebase_config

import smtplib
import random
from email.message import EmailMessage


def email_sending(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    user = "doanchuyennganh.it@gmail.com"
    msg["from"] = user
    password = "yduhgmzilbfoqbgr"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


auth = firebase_config.firebase.auth()


def send_code(email):
    code = random.randint(100000, 999999)

    # create and send verified code to email
    subject = "Email verification"
    body = f"The code to verification your email is: {code}"
    if email == '':
        return -1
    else:
        email_sending(subject, body, email)
        return code


def login(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Login successfully")
        return True
    except:
        print("Can't sign-up")
        return False


def register(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Sign-up successfully")
        return True
    except:
        print("Can't sign-up")
        return False


print(send_code('thieugiakk.hhp@gmail.com'))