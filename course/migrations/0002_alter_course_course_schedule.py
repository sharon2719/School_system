# Generated by Django 3.2.6 on 2021-08-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_schedule',
            field=models.FileField(blank='True', upload_to='documents/'),
        ),
    ]
