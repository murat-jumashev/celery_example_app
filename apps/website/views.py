from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


def send_email(current_site, user, email_template):
    mail_subject = 'New employee needs activation.'
    message = render_to_string(email_template, {
        'user': user,
        'domain': current_site.domain,
    })
    to_email = settings.ADMIN_EMAIL
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()


def index(request):
    current_site = get_current_site(request)
    user = request.user
    email_template = "website/email.html"
    send_email(current_site, user, email_template)
    return render(request, "website/index.html")