# Generated by Django 5.0.3 on 2024-04-02 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0004_pet_pet_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cid',
        ),
        migrations.AlterField(
            model_name='customer',
            name='emailId',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalPrice', models.FloatField(default=0.0)),
                ('emailId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetApp.customer')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetApp.pet')),
            ],
        ),
    ]
