# Generated by Django 2.1.3 on 2018-11-27 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20181126_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='desc_achieved_0',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='desc_technical_0',
            field=models.TextField(blank=True),
        ),
    ]