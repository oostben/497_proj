# Generated by Django 3.1.2 on 2020-11-02 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketswap', '0004_auto_20201026_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
    ]
