# Generated by Django 2.1.7 on 2019-03-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190309_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblogpreview',
            name='title',
            field=models.ForeignKey(default=1, on_delete='models.SET_DEFAULT', to='weblog.Weblog'),
        ),
    ]
