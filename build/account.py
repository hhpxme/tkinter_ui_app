import firebase_config

import smtplib
import random
from email.message import EmailMessage


list_admin = ['hhpxme@gmail.com']


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


def login(email, password):
    try:
        c_user = auth.sign_in_with_email_and_password(email, password)
        infor = auth.get_account_info(c_user['idToken'])
        for i in infor['users']:
            if i['emailVerified']:
                if email in list_admin:
                    return 1
                else:
                    return 0
            else:
                return -2
    except:
        return -1


def register(email, password):
    user_sign_up = auth.create_user_with_email_and_password(email, password)
    infor = auth.get_account_info(user_sign_up['idToken'])
    for i in infor['users']:
        return i['emailVerified']

