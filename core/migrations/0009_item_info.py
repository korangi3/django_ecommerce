# Generated by Django 2.2 on 2019-09-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190821_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]
