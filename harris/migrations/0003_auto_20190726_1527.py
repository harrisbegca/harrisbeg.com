# Generated by Django 2.2.3 on 2019-07-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harris', '0002_auto_20190726_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=1500),
        ),
    ]
