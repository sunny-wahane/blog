import os
from flask import url_for
from flask_mail import Message
from PIL import Image
import secrets
from your_blogs import app, mail


def save_avatar(file):
    random_hex = secrets.token_hex(8)
    _, f_extenstion = os.path.splitext(file.filename)
    random_file_name = random_hex + f_extenstion
    avatar_path = os.path.join(app.root_path, 'static', random_file_name)

    output_size = (125,125)
    i = Image.open(file)
    i.thumbnail(output_size)

    i.save(avatar_path)

    return random_file_name

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
        sender = 'sunnywahane14@gmail', 
        recipients=[user.email])
    msg.body =  f''' To reset your password, visit the following link:
{ url_for('users.reset_token', token=token, _external=True) }

If you did not make this request simply ignore this mail
'''
    mail.send(msg)
    