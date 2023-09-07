# Generated by Django 4.1.7 on 2023-04-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_registration_create_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration_create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration_data',
            name='password',
        ),
        migrations.RemoveField(
            model_name='registration_data',
            name='uname',
        ),
    ]
