# Generated by Django 3.0.5 on 2020-05-19 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_commentqa_postqa'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_color',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
