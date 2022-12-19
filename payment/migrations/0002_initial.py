# Generated by Django 4.1.4 on 2022-12-19 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expiredpayment',
            name='payment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentuser'),
        ),
    ]
