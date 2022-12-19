from rest_framework import serializers
from .models import User
from payment.models import Service,PaymentUser,ExpiredPayment

class ServiceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=80)
    description = serializers.CharField(max_length=45)
    logo = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Service
        fields = ["name", "description", "logo"]  

class PaymentUserSerializer(serializers.ModelSerializer):
    user= serializers.CharField(max_length=80)
    #service = serializers.
    #amount = serializers.
    #payment_date= serializers.DateField(blank=True)
    #expiration_date = serializers.DateField(blank=True)

    class Meta:
        model = Service
        fields = '__all__'

class ExpiredPaymentSerializer(serializers.ModelSerializer):
    #payment_user = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    #penalty_free_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


    class Meta:
        model = Service
        fields = '__all__'