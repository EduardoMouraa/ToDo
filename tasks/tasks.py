from __future__ import absolute_import, unicode_literals
from celery import shared_task

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import decouple


USERNAME = decouple.config('USERNAME', cast=str)
PASSWORD = decouple.config('PASSWORD', cast=str)
HOST = decouple.config('HOST', cast=str)
PORT = decouple.config('PORT', cast=int)


@shared_task
def exec1(opa):
    sendEmail()
    return opa 

    

def sendEmail():
    server = smtplib.SMTP(HOST, PORT)

    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)

    message = 'Olá, mundo!'
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = USERNAME
    email_msg['To'] = 'eduardoed18@hotmail.com'
    email_msg['Subject'] = 'Assunto da mensagem'
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    msg = 'E aeeeeeeeeeeeeee'
    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(USERNAME,'eduardoed18@hotmail.com', email_msg.as_string())
    print('Mensagem enviada!')
    server.quit()
    return ''