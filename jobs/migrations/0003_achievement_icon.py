# Generated by Django 3.0.5 on 2020-05-06 02:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_achievement'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='icon',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
