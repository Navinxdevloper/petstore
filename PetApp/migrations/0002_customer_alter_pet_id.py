# Generated by Django 5.0.3 on 2024-03-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('emailId', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('contactNo', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
