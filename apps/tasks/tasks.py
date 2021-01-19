from __future__ import absolute_import, unicode_literals
from celery import shared_task

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import decouple
from .models import Task

USERNAME = decouple.config('USERNAME', cast=str)
PASSWORD = decouple.config('PASSWORD', cast=str)
HOST = decouple.config('HOST', cast=str)
PORT = decouple.config('PORT', cast=int)


@shared_task
def exec1(data):
    task = Task.objects.get(id=data['id_task'])
    if task.done != 'done':
        sendEmail(task.user.email, task.title, task.description)

    return data 

    

def sendEmail(destination_email,title, msg):
    server = smtplib.SMTP(HOST, PORT)

    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)

    message = 'Tarefa atrasada. A descrição da tarefa se encontra logo abaixo.\n\n"{}"'.format(msg)
    email_msg = MIMEMultipart()
    email_msg['From'] = USERNAME
    email_msg['To'] = 'eduardoed18@hotmail.com' ## destination_email
    email_msg['Subject'] = 'A tarefa "{}" está atrasada!'.format(title)
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    server.sendmail(USERNAME,'eduardoed18@hotmail.com', email_msg.as_string())
    server.quit()
    return ''