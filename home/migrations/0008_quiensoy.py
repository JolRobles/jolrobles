# Generated by Django 3.2.18 on 2023-08-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_proyecto_tipo_proyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuienSoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'QuienSoy',
                'verbose_name_plural': 'QuienSoy',
            },
        ),
    ]
