from django_filters import rest_framework as filters
from payment.models import PaymentUser
from django import forms 

class PaymentUserFilter(filters.FilterSet):    
    class Meta:
        model = PaymentUser
        fields = {
            "payment_date":['gte'],
            "expiration_date":['lte']
        }

   