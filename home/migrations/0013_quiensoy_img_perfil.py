# Generated by Django 3.2.18 on 2023-08-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_respuestablog_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiensoy',
            name='img_perfil',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
