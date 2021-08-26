# Generated by Django 3.2.5 on 2021-08-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('age', models.PositiveSmallIntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('nationality', models.CharField(max_length=30)),
                ('county_or_district', models.CharField(max_length=25)),
                ('national_id', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('bio', models.TextField(max_length=500)),
                ('contract', models.FileField(blank='True', upload_to='Uploads')),
                ('date_hired', models.DateField()),
                ('languages', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]