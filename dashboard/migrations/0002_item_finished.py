# Generated by Django 2.2.7 on 2019-11-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='Выкуплен?'),
        ),
    ]
