# Generated by Django 3.2.6 on 2021-08-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_auto_20210812_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
