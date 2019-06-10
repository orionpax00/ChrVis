from __future__ import absolute_import, unicode_literals
from celery import shared_task

from . import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def sendMail():
    send_mail.send_mail()
