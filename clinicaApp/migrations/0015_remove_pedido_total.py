# Generated by Django 3.1.2 on 2020-11-18 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0014_auto_20201118_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='total',
        ),
    ]
