# Generated by Django 3.0.4 on 2020-04-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20200413_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discente',
            name='matricula',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
