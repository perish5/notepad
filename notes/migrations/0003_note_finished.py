# Generated by Django 2.2.2 on 2020-10-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20201017_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
