# Generated by Django 4.1.7 on 2023-04-26 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_workers_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers_data',
            name='image_face',
            field=models.ImageField(upload_to='images/'),
        ),
    ]