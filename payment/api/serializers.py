from rest_framework import serializers
from payment.models import Service,PaymentUser,ExpiredPayment

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["name", "description", "logo"]  

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id":instance.id,
            "user":instance.user.email,
            "service":instance.service.name,
            "amount":instance.amount,
            "payment_date":instance.payment_date,
            "expiration_date":instance.expiration_date
        }

class ExpiredPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayment
        fields = '__all__'