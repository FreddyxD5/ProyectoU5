from rest_framework import serializers
from payment.models import Service,PaymentUser,ExpiredPayment

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id","name", "description", "logo"]  

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

    # def validate(self,data):
    #     if data['payment_date'] > data['expiration_date']:
    #         raise serializers.ValidationError('La fecha de vencimiento no puede ser antes que la fecha de pago')
    #     return data

    # def save(self,data):
    #     if self.validated_data['payment_date'] > self.validated_data['expiration_date']:
    #         ExpiredPayment.objects.create()
    #     return data

class ExpiredPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayment
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id":instance.id,
            "user":instance.payment_user.user.email,
            "service":instance.payment_user.service.name,
            "penalty_free_amount":instance.penalty_free_amount
        }