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
    return "Creacion de usuarios morosos realizada con exito."
