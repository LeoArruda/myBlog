# Generated by Django 2.2 on 2020-01-04 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='first_name',
            field=models.TextField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='last_name',
            field=models.TextField(max_length=60, null=True),
        ),
    ]
