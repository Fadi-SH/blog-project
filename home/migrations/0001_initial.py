# Generated by Django 2.1.7 on 2019-02-20 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.date(2019, 2, 20))),
                ('body', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
