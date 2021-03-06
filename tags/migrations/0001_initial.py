# Generated by Django 2.2 on 2019-09-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_auto_20190821_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(blank=True, to='core.Item')),
            ],
        ),
    ]
