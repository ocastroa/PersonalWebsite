# Generated by Django 2.1.3 on 2018-12-19 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20181216_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='photo_main_portfolio',
        ),
    ]
