# Generated by Django 4.1.7 on 2023-04-27 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_workers_data_image_face'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers_data',
            name='image_face',
            field=models.ImageField(db_column='image', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='workers_data',
            name='image_work',
            field=models.ImageField(db_column='photo', upload_to='images'),
        ),
    ]