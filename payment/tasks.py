from random import random
from time import sleep
from celery import shared_task
from payment.models import PaymentUser
from django.conf import settings



@shared_task
def create_payment_expired():    
    payment_list = PaymentUser.objects.all()
    users_with_debt = []
    for user_payment in payment_list:
        if user_payment.fecha_limite:
            users_with_debt.append(user_payment)

    for user_debt in user_with_debts:
        ExpiredPayment.objects.create(payment_user= user_debt, penalty_free_amount=round(random()*100,2))
    return "Creacion de usuarios morosos con exito."

@shared_task
def add(x,y):
    return x+y




# @shared_task
# def count_books():
#     return Book.objects.count()

# from django.core.mail import send_mail

# @shared_task
# def enviar_correo(cabecera, cuerpo, email):
#     send_mail(cabecera,cuerpo,
#         settings.EMAIL_HOST_USER,
#         [email],
#         fail_silently = False
#     )
#     return "Se envio el correo correctamente."
    