from rest_framework import serializers
from payment.models import Service,PaymentUser,ExpiredPayment

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["name", "description", "logo"]  

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ExpiredPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'