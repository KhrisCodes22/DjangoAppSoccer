# Generated by Django 2.1 on 2019-11-01 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalevent',
            name='gameID',
            field=models.IntegerField(),
        ),
    ]
