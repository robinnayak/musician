# Generated by Django 3.0.8 on 2020-08-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_musician_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
