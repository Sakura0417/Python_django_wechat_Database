# Generated by Django 3.0 on 2020-04-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JDcommodityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=256)),
                ('productimg', models.CharField(max_length=128)),
                ('productprice', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ToutiaoIInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('auther', models.CharField(max_length=16)),
                ('date', models.DateField()),
                ('img', models.CharField(max_length=128)),
                ('linkaddress', models.CharField(max_length=128)),
            ],
        ),
    ]