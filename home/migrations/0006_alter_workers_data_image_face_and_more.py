# Generated by Django 4.1.7 on 2023-04-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_workers_data_image_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers_data',
            name='image_face',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='workers_data',
            name='image_work',
            field=models.FileField(upload_to='images/'),
        ),
    ]
