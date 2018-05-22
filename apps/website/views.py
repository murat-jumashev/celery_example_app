from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from .tasks import send_email_async


def send_email_to_admin(request):
    email_template = "website/email.html"
    current_site = get_current_site(request)

    mail_subject = 'New employee needs activation.'
    message = render_to_string(email_template, {
        'user': request.user,
        'domain': current_site.domain,
    })
    to_email = settings.ADMIN_EMAIL

    send_email_async.delay(mail_subject, message, to_email)


class IndexView(TemplateView):
    template_name = "website/index.html"

    def get(self, request):
        send_email_to_admin(request)
        return super().get(request)
