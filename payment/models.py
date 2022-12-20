from datetime import datetime
from django.db import models
from users.models import Usuario


class Service(models.Model):
    name = models.CharField('Nombre de Servicio', max_length=255)
    description = models.TextField('Descripcion del Servicio')
    logo = models.URLField(("URL de logo"), max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class PaymentUser(models.Model):
    user= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)
    payment_date = models.DateField(blank=True)
    expiration_date = models.DateField(blank=True)
    deuda_vigente = models.BooleanField(default=True)


    def obtener_email_user(self):
        return self.user.email

    @property
    def fecha_limite(self):
        if self.expiration_date is not None:
            if datetime.now() > expiration_date:
                self.deuda_vigente = False
                self.save()
                return True
            return False
        return False


    def __str__(self):
        return f"Recibo de {self.obtener_email_user()} por: {self.service.name}"


class ExpiredPayment(models.Model):
    payment_user = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    penalty_free_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"Recibo Expirado de {self.payment_user.obtener_email_user()} por S./{self.penalty_free_amount}"
    
