# Generated by Django 3.0.8 on 2020-07-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
    ]
