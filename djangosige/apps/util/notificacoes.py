from djangosige.configs import settings
from notifications.signals import notify
from django.core.mail import send_mail

def send_notification(user, verb, description):
    try:
        notify.send(user, recipient=user, verb=verb, description=description)
    except Exception as e:
        pass

    try:
        if user.email:
            send_mail(
                '[Notificação de teste]: ' + verb,
                description, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=True,)
    except Exception as e:
        pass

def save_handler(sender, instance, created, **kwargs):
    try:
        notify.send(instance, verb='alterado')
    except:
        pass

