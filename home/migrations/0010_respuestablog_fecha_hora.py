# Generated by Django 3.2.18 on 2023-08-11 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_respuestablog'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestablog',
            name='fecha_hora',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
