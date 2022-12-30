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
            "logo":instance.service.logo if instance.service.logo is not None else '',
            "amount":instance.amount,
            "payment_date":instance.payment_date,
            "deuda_vigente":instance.deuda_vigente,
            "expiration_date":instance.expiration_date
        }
    

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
            "monto":instance.payment_user.amount,
            "logo":instance.payment_user.service.logo,
            "service":instance.payment_user.service.name,
            "deuda_vigente":instance.payment_user.deuda_vigente,
            "expiration_date":instance.payment_user.expiration_date,
            "penalty_free_amount":instance.penalty_free_amount
        }