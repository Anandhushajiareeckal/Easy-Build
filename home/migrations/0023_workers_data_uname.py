# Generated by Django 4.1.7 on 2023-05-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_registration_data_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers_data',
            name='uname',
            field=models.CharField(default='0', max_length=100),
        ),
    ]