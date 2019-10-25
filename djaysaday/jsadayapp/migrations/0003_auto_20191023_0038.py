# Generated by Django 2.2.6 on 2019-10-23 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsadayapp', '0002_auto_20191023_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humor',
            name='nivel',
            field=models.CharField(choices=[(-2, 'Muito negativo'), (-1, 'Negativo'), (0, 'Neutro'), (1, 'Positivo'), (2, 'Muito positivo')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='sensacao',
            name='nivel',
            field=models.CharField(choices=[(-2, 'Muito negativo'), (-1, 'Negativo'), (0, 'Neutro'), (1, 'Positivo'), (2, 'Muito positivo')], default=0, max_length=1),
        ),
    ]