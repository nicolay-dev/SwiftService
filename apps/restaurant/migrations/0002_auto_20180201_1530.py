# Generated by Django 2.0.1 on 2018-02-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='slug',
            field=models.CharField(blank=True, editable=False, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('V', 'Visitante'), ('E', 'Editor'), ('A', 'Autentificado'), ('R', 'Administrador')], max_length=1),
        ),
    ]