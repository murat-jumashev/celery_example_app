from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task
def send_email_async(mail_subject, message, to_email):
    # for faking a long running task
    import time; time.sleep(10)

    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
