# Generated by Django 3.0.7 on 2020-07-13 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0003_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_full_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
