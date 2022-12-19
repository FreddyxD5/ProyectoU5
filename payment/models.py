from django.db import models

class Service(models.Model):
    name = models.CharField('Nombre de Servicio', max_length=255)
    description = models.TextField('Descripcion del Servicio')
    logo = models.URLField(("URL de logo"), max_length=200)

    def __str__(self):
        return f"{self.name}"


class PaymentUser(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)
    payment_date = models.DateField(blank=True)
    expiration_date = models.DateField(blank=True)


class ExpiredPayment(models.Model):
    payment_user = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    penalty_free_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
