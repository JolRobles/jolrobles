# Generated by Django 3.2.18 on 2023-08-11 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_quiensoy'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.blog')),
            ],
            options={
                'verbose_name': 'RespuestaBlog',
                'verbose_name_plural': 'RespuestasBlog',
            },
        ),
    ]