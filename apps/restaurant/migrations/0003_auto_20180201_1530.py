# Generated by Django 2.0.1 on 2018-02-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20180201_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('E', 'Editor'), ('R', 'Administrador'), ('V', 'Visitante'), ('A', 'Autentificado')], max_length=1),
        ),
    ]