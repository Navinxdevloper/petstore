# Generated by Django 5.0.3 on 2024-04-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0005_remove_customer_cid_alter_customer_emailid_cartmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('adminEmailId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('adminpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
