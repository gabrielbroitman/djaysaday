# Generated by Django 2.2.5 on 2019-10-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsadayapp', '0003_auto_20191023_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humor',
            name='sensacoes',
            field=models.ManyToManyField(default=None, related_name='humores', to='jsadayapp.Sensacao'),
        ),
    ]