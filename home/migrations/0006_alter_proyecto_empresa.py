# Generated by Django 3.2.18 on 2023-08-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20230806_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='empresa',
            field=models.CharField(max_length=200),
        ),
    ]