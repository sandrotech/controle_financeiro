# Generated by Django 4.2.4 on 2023-08-23 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controle_financeiro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='DATA',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='MOVIMENTACAO',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='VALOR',
        ),
        migrations.AddField(
            model_name='registro',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='registro',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='movimentacao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
