# Generated by Django 4.1.7 on 2023-05-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_registration_data_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration_data',
            name='uname',
            field=models.CharField(default='0', max_length=100),
        ),
    ]