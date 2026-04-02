from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def send_to_email(email, first_name):
    subject = "Ro'yhatdan o'tish"
    message = f"{first_name} Bizni saytdan ro'yhatdan o'tdingiz!"
    send_mail(subject, message, EMAIL_HOST_USER, [email])
    return {'status': True, 'email': email, 'first_name': first_name}
