# Generated by Django 3.1.3 on 2021-02-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20210228_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
