# Generated by Django 3.2.9 on 2021-11-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('completa', 'Completa')], default='completa', max_length=8),
        ),
    ]
