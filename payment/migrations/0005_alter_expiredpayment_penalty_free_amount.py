# Generated by Django 4.1.3 on 2022-12-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_paymentuser_deuda_vigente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiredpayment',
            name='penalty_free_amount',
            field=models.DecimalField(decimal_places=2, default=45.02, max_digits=10),
        ),
    ]