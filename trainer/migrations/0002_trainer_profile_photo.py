# Generated by Django 3.2.5 on 2021-08-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
