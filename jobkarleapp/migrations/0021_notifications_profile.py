# Generated by Django 2.2.2 on 2020-05-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobkarleapp', '0020_notifications_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='Profile',
            field=models.FileField(null=True, upload_to='profile'),
        ),
    ]
