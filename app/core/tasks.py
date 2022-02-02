from django.conf import settings

from django.core.mail import send_mail
from app.celery import app


admin_email = settings.ADMIN_EMAIL


@app.task()
def send_registration_email_task(username, email):
    """task to send an email when a user registers"""
    return send_mail(
            'Welcome to IMDB-BACKEND',
            f"Hi {username}, \nThank you for joining us.",
            admin_email,
            [email],
            # fail_silently=False,
        )
