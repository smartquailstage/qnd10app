from celery import task
from django.core.mail import send_mail


@task
def Notificación(alert_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """
    subject = 'Notificación: Acceso prohibido al Sistema de información Secretaría de Cultura'
    message = 'Acaban de acceder al sistema de información de la secretaría de cultura'
    mail_sent = send_mail(subject,
                          message,
                          'info@smartquail.io',
                          'info@smartquail.io')
    return mail_sent